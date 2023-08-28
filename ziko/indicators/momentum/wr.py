import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class WilliamsR(BaseIndicator):
    NAME = 'WilliamsR'

    def __init__(self, period: int = 14, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = 'wr({},{})'.format(self.column, self.period)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.momentum.wr(data['high'], data['low'], data['close'], lbp=self.period)

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [-80, -80], '--', color='gray')
        axis.plot([data.index.min(), data.index.max()], [-20, -20], '--', color='gray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'period': self.period,
                'column': self.column
            }
        }
