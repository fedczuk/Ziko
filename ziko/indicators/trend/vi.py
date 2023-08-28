import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator
from ziko.indicators.partial import Partial


class VortexIndicator(BaseIndicator):
    NAME = 'VortexIndicator'

    def __init__(self, period: int = 14, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = None

        self._vi_diff = 'vi_diff({},{})'.format(self.column, self.period)
        self._vi_neg_col = 'vi_neg({},{})'.format(self.column, self.period)
        self._vi_pos_col = 'vi_pos({},{})'.format(self.column, self.period)

    @property
    def diff(self) -> Partial:
        return Partial(self._vi_diff, self)

    @property
    def neg(self) -> Partial:
        return Partial(self._vi_neg_col, self)

    @property
    def pos(self) -> Partial:
        return Partial(self._vi_pos_col, self)

    def calculate(self, data: DataFrame):
        indicator = ta.trend.VortexIndicator(data['high'], data['low'], data['close'], n=self.period)
        data[self._vi_diff] = indicator.vortex_indicator_diff()
        data[self._vi_neg_col] = indicator.vortex_indicator_neg()
        data[self._vi_pos_col] = indicator.vortex_indicator_pos()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self._vi_neg_col, self._vi_pos_col], axis, self.NAME)

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'period': self.period,
                'column': self.column
            }
        }
