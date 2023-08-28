import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class CommodityChannelIndex(BaseIndicator):
    NAME = 'CommodityChannelIndex'

    def __init__(self, n: int = 20, c: float = 0.015, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.n = n
        self.c = c
        self.name = 'cci({},{}-{})'.format(self.column, self.n, self.c)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.trend.cci(data['high'], data['low'], data['close'], n=self.n, c=self.c)

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [100, 100], '--', color='gray')
        axis.plot([data.index.min(), data.index.max()], [0, 0], '--', color='gray')
        axis.plot([data.index.min(), data.index.max()], [-100, -100], '--', color='gray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'n': self.n,
                'c': self.c,
                'column': self.column
            }
        }
