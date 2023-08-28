import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class DailyLogReturn(BaseIndicator):
    NAME = 'DailyLogReturn'

    def __init__(self, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.name = 'dlr({})'.format(self.column)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.others.daily_log_return(data['close'])

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'column': self.column
            }
        }
