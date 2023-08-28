from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class Column(BaseIndicator):
    def __init__(self, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)

    def calculate(self, data: DataFrame):
        pass
