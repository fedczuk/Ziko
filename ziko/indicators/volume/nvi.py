import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class NegativeVolumeIndex(BaseIndicator):
    NAME = 'NegativeVolumeIndex'

    def __init__(self, column: str='close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.name = 'nvi({})'.format(self.column)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.volume.negative_volume_index(data['close'], data['volume'])

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'column': self.column,
            }
        }
