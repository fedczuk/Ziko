from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class Partial(BaseIndicator):
    def __init__(self, column: str = 'close', parent=None, *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.parent = parent

    def calculate(self, data: DataFrame):
        if self.column not in data.columns:
            self.parent.calculate(data)
