from abc import ABCMeta, abstractmethod

CLASSIFIER_INITIALISED = 0
CLASSIFIER_READY = 1

class BasicClassifier(metaclass=ABCMeta):
    def __init__(self, delta: float):
        self.delta = delta
        self.status = CLASSIFIER_INITIALISED

    @abstractmethod
    def load(self):
        pass

    def setDelta(self, delta):
        self.delta = delta

    @abstractmethod
    def classify(self, lines: list) -> list:
        pass