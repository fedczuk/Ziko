import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class TrueStrengthIndex(BaseIndicator):
    NAME = 'TrueStrengthIndex'

    def __init__(self, r: int = 25, s: int = 13, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.r = r
        self.s = s
        self.name = 'tsi({},{}-{})'.format(self.column, self.r, self.s)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.momentum.tsi(data['close'], r=self.r, s=self.s)

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [0, 0], '--', color='gray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'r': self.r,
                's': self.s,
                'column': self.column
            }
        }
