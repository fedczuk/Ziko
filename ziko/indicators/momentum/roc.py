import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class RateOfChange(BaseIndicator):
    NAME = 'RateOfChange'

    def __init__(self, period: int = 14, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = 'roc({},{})'.format(self.column, self.period)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.momentum.roc(data['close'], n=self.period)

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [0, 0], '--', color='gray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'period': self.period,
                'column': self.column
            }
        }
