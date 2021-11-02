import pandas as pd

df = pd.read_csv("../data/AAPL_TIME_SERIES_DAILY.csv")
print(df.head())

class Stockdatalocal:
    """Class to get local stock data"""
    def __init__(self, data_folder_path: str = "../data/") -> None:
        self.data_folder_path = data_folder_path
