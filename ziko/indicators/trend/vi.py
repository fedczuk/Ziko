import ta

from ziko.indicators.base import BaseIndicator
from ziko.indicators.partial import Partial


class VortexIndicator(BaseIndicator):
    NAME = 'VortexIndicator'

    def __init__(self, period=14, column='close', *args, **kwargs):
        """
        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = None

        self._vi_diff = 'vi_diff({},{})'.format(self.column, self.period)
        self._vi_neg_col = 'vi_neg({},{})'.format(self.column, self.period)
        self._vi_pos_col = 'vi_pos({},{})'.format(self.column, self.period)

    @property
    def diff(self):
        return Partial(self._vi_diff, self)

    @property
    def neg(self):
        return Partial(self._vi_neg_col, self)

    @property
    def pos(self):
        return Partial(self._vi_pos_col, self)

    def calculate(self, data):
        """
        :param data:
        :type data: pandas.DataFrame
        """
        indicator = ta.trend.VortexIndicator(data['high'], data['low'], data['close'], n=self.period)
        data[self._vi_diff] = indicator.vortex_indicator_diff()
        data[self._vi_neg_col] = indicator.vortex_indicator_neg()
        data[self._vi_pos_col] = indicator.vortex_indicator_pos()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self._vi_neg_col, self._vi_pos_col], axis, self.NAME)

    def to_dict(self):
        """
        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'period': self.period,
                'column': self.column
            }
        }
