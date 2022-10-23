from Classifiers.ParaphraseClassifier import ParaphraseClassifier
from Frontend.BasicFrontend import BasicFrontend
from Frontend.TkFrontend import TkFrontend
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple sentence clusterization tool')
    parser.add_argument('--delta', dest='delta', action='store', default=0.33, help='Delta for classifier. The smaller '
                                                                                    'delta the smaller groups. '
                                                                                    'Default 0.33. For russian use '
                                                                                    '0.28')
    args = parser.parse_args()

    frontend: BasicFrontend = TkFrontend(classifier=ParaphraseClassifier(delta=args.delta))
    frontend.start()