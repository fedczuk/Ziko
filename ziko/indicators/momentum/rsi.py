import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class RelativeStrengthIndex(BaseIndicator):
    NAME = 'RSI'

    def __init__(self, period: int = 14, column: int = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = 'rsi({},{})'.format(self.column, self.period)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.momentum.rsi(data[self.column], window=self.period)

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [70, 70], '--', color='gray')
        axis.plot([data.index.min(), data.index.max()], [30, 30], '--', color='gray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'period': self.period,
                'column': self.column
            }
        }
