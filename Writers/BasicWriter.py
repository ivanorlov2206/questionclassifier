from abc import ABCMeta, abstractmethod


class BasicWriter(metaclass=ABCMeta):

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def write(self, predictionResult):
        pass