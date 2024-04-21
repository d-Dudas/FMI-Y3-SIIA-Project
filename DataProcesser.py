#!/bin/python3

from ProcessedProblemReportData import ProcessedProblemReportData
from ProblemReport import ProblemReport
from Serializer import Serialzier

from typing import Dict, List
import json
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
from sklearn import preprocessing
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy.sparse


class DataProcesser:
    def __init__(self, dataFile):
        self.__serializer = Serialzier()

        self.__input_data_filename: str = 'input.npz'
        self.__label_encoder_filename: str = 'label_encoder.pkl'
        self.__vectorizer_filename: str = 'vectorizer.pkl'
        self.__dict_vectorizer_filename: str = 'dict_vectorizer.pkl'

        if (
                self.__serializer.check_if_file_exists(self.__input_data_filename) and
                self.__serializer.check_if_file_exists(self.__label_encoder_filename) and
                self.__serializer.check_if_file_exists(self.__vectorizer_filename) and
                self.__serializer.check_if_file_exists(self.__dict_vectorizer_filename)):
            self.__input = self.__serializer.load_sparse_matrix(
                self.__input_data_filename)
            self.__label_encoder = self.__serializer.deserialize_object(
                self.__label_encoder_filename)
            self.__vectorizer = self.__serializer.deserialize_object(
                self.__vectorizer_filename)
            self.__dict_vectorizer = self.__serializer.deserialize_object(
                self.__dict_vectorizer_filename)
        else:
            self.__dataFile = dataFile
            self.__data: List[ProcessedProblemReportData] = []
            self.__label_encoder = preprocessing.LabelEncoder()
            self.__vectorizer = TfidfVectorizer(stop_words='english')
            self.__dict_vectorizer = DictVectorizer(sparse=True)
            self.__input: scipy.sparse.csr.csr_matrix = None

            self.__process()

    def __stemm_tokens(self, tokens: List[str]) -> List[str]:
        stemmer = nltk.PorterStemmer()
        return [stemmer.stem(token) for token in tokens]

    def __rejoin_stemmed_tokens(self, tokens: List[str]) -> str:
        return ' '.join(tokens)

    def __extract_useful_features(self, problem_report: ProblemReport) -> Dict[str, str | List[str]]:
        useful_features = {}
        useful_features['feature'] = "" if problem_report.feature == None else problem_report.feature.lower()
        useful_features['group_in_charge'] = problem_report.group_in_charge.lower()
        useful_features['release'] = [rls.lower()
                                      for rls in problem_report.release]

        return useful_features

    def __extract_title_and_description(self, problem_report: ProblemReport) -> str:
        title_and_description = problem_report.title + \
            ' ' + problem_report.description.__str__()
        title_and_description_tokens = nltk.word_tokenize(
            title_and_description)

        stemmed_title_and_description_tokekens = self.__stemm_tokens(
            title_and_description_tokens)

        processed_title_and_description = self.__rejoin_stemmed_tokens(
            stemmed_title_and_description_tokekens)

        return processed_title_and_description

    def __extract_data(self, problem_report: ProblemReport):
        processed_title_and_description: str = self.__extract_title_and_description(
            problem_report)

        useful_features: Dict[str, str | List[str]
                              ] = self.__extract_useful_features(problem_report)

        processed_problem_report_data: ProcessedProblemReportData = ProcessedProblemReportData(
            processed_title_and_description, useful_features, problem_report.state)

        self.__data.append(processed_problem_report_data)

    def __encode_labels(self) -> None:
        labels = set(data.label for data in self.__data)
        self.__label_encoder.fit_transform(list(labels))

        for data in self.__data:
            data.encoded_label = self.__label_encoder.transform([data.label])[
                0]

    def __compute_input(self) -> None:
        title_and_description_vector = self.__vectorizer.fit_transform(
            [data.processed_title_and_description for data in self.__data])

        useful_features_vector = self.__dict_vectorizer.fit_transform(
            [data.useful_features for data in self.__data])

        self.__input = scipy.sparse.hstack(
            [title_and_description_vector, useful_features_vector])

    def __process(self) -> None:
        with open(self.__dataFile, 'r') as file:
            data = json.load(file)
            prontos = data['values']
            for pronto in prontos:
                problem_report = ProblemReport.from_dict(pronto)
                self.__extract_data(problem_report)

        self.__encode_labels()
        self.__compute_input()

    def get_input(self) -> scipy.sparse.csr.csr_matrix:
        return self.__input

    def save(self) -> None:
        self.__serializer.save_sparse_matrix(
            self.__input_data_filename, self.__input)
        self.__serializer.serialize_object(
            self.__label_encoder_filename, self.__label_encoder)
        self.__serializer.serialize_object(
            self.__vectorizer_filename, self.__vectorizer)
        self.__serializer.serialize_object(
            self.__dict_vectorizer_filename, self.__dict_vectorizer)
