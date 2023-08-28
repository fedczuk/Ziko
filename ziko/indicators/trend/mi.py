import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class MassIndex(BaseIndicator):
    NAME = 'MassIndex'

    def __init__(self, n: int = 9, n2: int = 25, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.n = n
        self.n2 = n2
        self.name = 'mi({},{})'.format(self.column, self.n, self.n2)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.trend.mass_index(data['high'], data['low'], n=self.n, n2=self.n2)

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'n': self.n,
                'n2': self.n2,
                'column': self.column
            }
        }
