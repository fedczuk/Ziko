import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class KaufmanAdaptiveMovingAverage(BaseIndicator):
    NAME = 'KaufmanAdaptiveMovingAverage'

    def __init__(self, n: int = 10, pow1: int = 2, pow2: int = 30, column: int = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.n = n
        self.pow1 = pow1
        self.pow2 = pow2
        self.name = 'kama({},{}-{}-{})'.format(self.column, self.n, self.pow1, self.pow2)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.momentum.kama(
            data['close'], n=self.n, pow1=self.pow1, pow2=self.pow2
        )

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        plot.indicators(data, [self.column], axis, self.NAME)

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'n': self.n,
                'pow1': self.pow1,
                'pow2': self.pow2,
                'column': self.column
            }
        }
