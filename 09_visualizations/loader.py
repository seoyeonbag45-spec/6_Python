import pandas as pd

from config import path, ENCODING


def load_prices():
    return pd.read_csv(path('prices.csv'), encoding=ENCODING, parse_dates=['date'])

def load_companies():
    return pd.read_csv(path('companies.csv'), encoding=ENCODING)

def load_sectors():
    return pd.read_csv(path('sectors.csv'), encoding=ENCODING)