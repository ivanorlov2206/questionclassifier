import pandas as pd


def proceedXLS(path: str, column: str) -> list:
    xls = pd.read_excel(path, usecols=column)
    arr = [x[0] for x in xls.values]
    return arr
