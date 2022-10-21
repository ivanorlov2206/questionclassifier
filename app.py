from Classifiers.ParaphraseClassifier import ParaphraseClassifier
from Frontend.BasicFrontend import BasicFrontend
from Frontend.TkFrontend import TkFrontend

if __name__ == "__main__":
    frontend: BasicFrontend = TkFrontend(classifier=ParaphraseClassifier(delta=0.28))
    frontend.start()