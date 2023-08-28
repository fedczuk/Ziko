import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class OnBalanceVolume(BaseIndicator):
    NAME = 'OBV'

    def __init__(self, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.name = 'obv({})'.format(self.column)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.volume.on_balance_volume(data['close'], data['volume'])

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [0, 0], '--', color='lightgray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'column': self.column
            }
        }
