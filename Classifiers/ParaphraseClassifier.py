from sentence_transformers import SentenceTransformer

from Classifiers.BasicClassifier import BasicClassifier, CLASSIFIER_READY
from Common.PredictionGroup import PredictionGroup
from Common.PredictionResult import PredictionResult
from Utils.MathUtils import cosDistAndCheckDelta


class ParaphraseClassifier(BasicClassifier):
    def __init__(self, delta: float):
        BasicClassifier.__init__(self, delta)

    def load(self):
        self.model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
        self.status = CLASSIFIER_READY

    def _predict(self, lines: list):
        if self.status != CLASSIFIER_READY:
            return None
        embeddings = self.model.encode(lines)

        nonVisitedSentenceNumbers = set(range(len(lines)))
        predictionGroups = []
        for i in range(len(lines)):
            if not i in nonVisitedSentenceNumbers:
                continue
            tempGroup = []
            for j in range(len(lines)):
                if j in nonVisitedSentenceNumbers and cosDistAndCheckDelta(embeddings[i], embeddings[j], self.delta):
                    nonVisitedSentenceNumbers.remove(j)
                    tempGroup.append((j, lines[j]))
            if len(tempGroup) > 0:
                predictionGroups.append(PredictionGroup(tempGroup))
        predictionGroups.sort(key=lambda x: x.length, reverse=True)

        return PredictionResult(predictionGroups)

    def classify(self, lines: list) -> PredictionResult:
        return self._predict(lines)