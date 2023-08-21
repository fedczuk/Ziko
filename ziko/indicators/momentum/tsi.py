import ta

from ziko.indicators.base import BaseIndicator


class TrueStrengthIndex(BaseIndicator):
    NAME = 'TrueStrengthIndex'

    def __init__(self, r=25, s=13, column='close', *args, **kwargs):
        """
        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.r = r
        self.s = s
        self.name = 'tsi({},{}-{})'.format(self.column, self.r, self.s)

    def calculate(self, data):
        """
        :param data:
        :type data: pandas.DataFrame
        """
        data[self.name] = ta.momentum.tsi(data['close'], r=self.r, s=self.s)

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [0, 0], '--', color='gray')

    def to_dict(self):
        """
        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'r': self.r,
                's': self.s,
                'column': self.column
            }
        }
