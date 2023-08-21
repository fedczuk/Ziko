import os

import pandas as pd


class Quote(object):
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def get(self, date, column, nearest=False):
        try:
            return self.data.loc[date, column]
        except:
            if nearest:
                index = pd.Series(self.data.index)
                index = index[index >= date]
                return self.data.loc[index.min(), column]
            return None

    @classmethod
    def from_csv(cls, filename, begin_date=None, end_date=None):
        ticker = os.path.splitext(os.path.basename(filename))[0]

        df = pd.read_csv(filename)
        df.columns = [c.lower().strip('<>') for c in df.columns]
        df['date'] = pd.to_datetime(df['date'], format="%Y%m%d")

        if begin_date is not None:
            df = df[df['date'] >= begin_date]

        if end_date is not None:
            df = df[df['date'] <= end_date]

        df = df.set_index('date')
        df = df.rename(columns={"vol": "volume"})

        return cls(ticker, df)
