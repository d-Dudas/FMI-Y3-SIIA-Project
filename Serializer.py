import os
import pickle
from scipy.sparse import save_npz, load_npz


class Serialzier:
    def __init__(self, serialized_data_folder: str = "./data/"):
        self.__data_folder = serialized_data_folder

    def save_sparse_matrix(self, filename, matrix):
        filename = self.__data_folder + filename
        save_npz(filename, matrix)

    def load_sparse_matrix(self, filename):
        filename = self.__data_folder + filename

        return load_npz(filename)

    def serialize_object(self, filename, data):
        filename = self.__data_folder + filename
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

    def deserialize_object(self, filename):
        filename = self.__data_folder + filename
        with open(filename, 'rb') as f:
            object = pickle.load(f)

        return object

    def check_if_file_exists(self, filename) -> bool:
        filename = self.__data_folder + filename

        return os.path.exists(filename)
