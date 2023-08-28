import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class AverageTrueRange(BaseIndicator):
    NAME = 'ATR'

    def __init__(self, period: int = 14, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = 'atr({},{})'.format(self.column, self.period)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.volatility.average_true_range(data['high'], data['low'], data['close'], n=self.period)

    def plot(self, plot, axis, data):
        plot.indicators(data[data[self.name] > 0], [self.name], axis, self.NAME)

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'column': self.column,
                'period': self.period
            }
        }
