import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class EaseOfMovement(BaseIndicator):
    NAME = 'EaseOfMovement'

    def __init__(self, period: int = 14, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = 'eom({},{})'.format(self.column, self.period)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.volume.ease_of_movement(data['high'], data['low'], data['volume'], n=self.period)

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [0, 0], '--', color='lightgray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'column': self.column,
                'period': self.period
            }
        }
