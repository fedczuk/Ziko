import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator
from ziko.indicators.column import Column


class MovingAverageConvergenceDivergence(BaseIndicator):
    NAME = 'MACD'

    def __init__(self, slow: int = 26, fast: int = 12, sign: int = 9, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.slow = slow
        self.fast = fast
        self.sign = sign
        self.name = None

        self._macd_col = 'macd({},{}-{}-{})'.format(self.column, self.slow, self.fast, self.sign)
        self._macd_diff_col = 'macd_diff({},{}-{}-{})'.format(self.column, self.slow, self.fast, self.sign)
        self._macd_signal_col = 'macd_sig({},{}-{}-{})'.format(self.column, self.slow, self.fast, self.sign)

    @property
    def macd(self) -> Column:
        return Column(self._macd_col)

    @property
    def diff(self) -> Column:
        return Column(self._macd_diff_col)

    @property
    def signal(self) -> Column:
        return Column(self._macd_signal_col)

    def calculate(self, data: DataFrame):
        indicator = ta.trend.MACD(data[self.column], self.slow, self.fast, self.sign)
        data[self._macd_col] = indicator.macd()
        data[self._macd_diff_col] = indicator.macd_diff()
        data[self._macd_signal_col] = indicator.macd_signal()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self._macd_col, self._macd_signal_col], axis, self.NAME)

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'slow': self.slow,
                'fast': self.fast,
                'sign': self.sign,
                'column': self.column
            }
        }
