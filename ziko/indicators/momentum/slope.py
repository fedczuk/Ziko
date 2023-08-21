from ziko.indicators.base import BaseIndicator
import numpy as np
from scipy import stats


class SlopeIndicator(BaseIndicator):
    def __init__(self, period=250, column='close', *args, **kwargs):
        """

        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = 'mom({},{})'.format(self.column, self.period)

    @staticmethod
    def _score(ts):
        x = np.arange(len(ts))
        regress = stats.linregress(x, np.log(ts))
        slope = regress[0]
        return slope * regress[2] ** 2

    def calculate(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        """
        data[self.name] = data[self.column].rolling(self.period).apply(self._score)

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
