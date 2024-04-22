from typing import List, Dict
import tensorflow as tf
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Dense, Input, Dropout  # type: ignore
from tensorflow.keras.utils import to_categorical  # type: ignore
from sklearn.model_selection import train_test_split

from Serializer import Serialzier


class Model:
    def __init__(self, labels, input):
        self.__serializer = Serialzier()

        self.__model_filename: str = 'model.keras'
        self.__model_file_path: str = 'data/' + self.__model_filename

        if self.__serializer.check_if_file_exists(self.__model_filename):
            self.__model = tf.keras.models.load_model(self.__model_file_path)
        else:
            print("File not found")
            self.__build_model(labels, input)
            self.__model.save(self.__model_file_path)

    def __build_model(self, labels, input) -> None:
        number_of_labels = len(set(labels))
        self.__model = Sequential([
            Input(shape=(input.shape[1],)),
            Dense(128, activation='relu'),
            Dropout(0.5),
            Dense(64, activation='relu'),
            Dropout(0.5),
            Dense(units=number_of_labels, activation='softmax')
        ])
        self.__model.compile(loss='categorical_crossentropy',
                             optimizer='adam', metrics=['accuracy'])

        labels_encoded = to_categorical(labels, num_classes=number_of_labels)
        x_train, x_test, y_train, y_test = train_test_split(
            input, labels_encoded, test_size=0.2)

        self.__model.fit(x_train, y_train, epochs=50,
                         batch_size=32, validation_split=0.1)
        self.__test_loss, self.__test_accuracy = self.__model.evaluate(
            x_test, y_test)
        print(f'Test loss: {self.__test_loss}')
        print(f'Test accuracy: {self.__test_accuracy}')

    def predict(self, input):
        prediction = self.__model.predict(input)
        predicted_label = tf.argmax(prediction, axis=1)
        return predicted_label[0]
