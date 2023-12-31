import ta

from ziko.indicators.base import BaseIndicator
from ziko.indicators.partial import Partial


class AroonIndicator(BaseIndicator):
    NAME = 'AroonIndicator'

    def __init__(self, period=25, column='close', *args, **kwargs):
        """
        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = None

        self._ai_col = 'ai({},{})'.format(self.column, self.period)
        self._ai_down_col = 'ai_down({},{})'.format(self.column, self.period)
        self._ai_up_col = 'ai_up({},{})'.format(self.column, self.period)

    @property
    def ai(self):
        return Partial(self._ai_col, self)

    @property
    def ai_down(self):
        return Partial(self._ai_down_col, self)

    @property
    def ai_up(self):
        return Partial(self._ai_up_col, self)

    def calculate(self, data):
        """
        :param data:
        :type data: pandas.DataFrame
        """
        indicator = ta.trend.AroonIndicator(data['close'], window=self.period)
        data[self._ai_col] = indicator.aroon_indicator()
        data[self._ai_down_col] = indicator.aroon_down()
        data[self._ai_up_col] = indicator.aroon_up()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self._ai_down_col, self._ai_up_col], axis, self.NAME)

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
