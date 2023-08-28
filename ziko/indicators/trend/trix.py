import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class Trix(BaseIndicator):
    NAME = 'Trix'

    def __init__(self, period: int = 15, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = 'trix({},{})'.format(self.column, self.period)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.trend.trix(data['close'], n=self.period)

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [0, 0], '--', color='lightgray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'period': self.period,
                'column': self.column
            }
        }
