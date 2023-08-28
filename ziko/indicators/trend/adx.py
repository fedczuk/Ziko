import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator
from ziko.indicators.partial import Partial


class AverageDirectionalMovement(BaseIndicator):
    NAME = 'ADX'

    def __init__(self, period: int = 14, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = None

        self._adx_col = 'adx({},{})'.format(self.column, self.period)
        self._adx_neg_col = 'adx_neg({},{})'.format(self.column, self.period)
        self._adx_pos_col = 'adx_pos({},{})'.format(self.column, self.period)

    @property
    def adx(self) -> Partial:
        return Partial(self._adx_col, self)

    @property
    def adx_neg(self) -> Partial:
        return Partial(self._adx_neg_col, self)

    @property
    def adx_pos(self) -> Partial:
        return Partial(self._adx_pos_col, self)

    def calculate(self, data: DataFrame):
        indicator = ta.trend.ADXIndicator(data['high'], data['low'], data['close'], window=self.period)
        data[self._adx_col] = indicator.adx()
        data[self._adx_neg_col] = indicator.adx_neg()
        data[self._adx_pos_col] = indicator.adx_pos()

    def plot(self, plot, axis, data):
        # self._adx_neg_col, self._adx_pos_col
        plot.indicators(data[data[self._adx_col] > 0], [self._adx_col], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [25, 25], '--', color='gray')
        axis.plot([data.index.min(), data.index.max()], [20, 20], '--', color='gray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'period': self.period,
                'column': self.column
            }
        }
