import ta

from ziko.indicators.base import BaseIndicator


class CommodityChannelIndex(BaseIndicator):
    NAME = 'CommodityChannelIndex'

    def __init__(self, n=20, c=0.015, column='close', *args, **kwargs):
        """
        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.n = n
        self.c = c
        self.name = 'cci({},{}-{})'.format(self.column, self.n, self.c)

    def calculate(self, data):
        """
        :param data:
        :type data: pandas.DataFrame
        """
        data[self.name] = ta.trend.cci(data['high'], data['low'], data['close'], n=self.n, c=self.c)

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [100, 100], '--', color='gray')
        axis.plot([data.index.min(), data.index.max()], [0, 0], '--', color='gray')
        axis.plot([data.index.min(), data.index.max()], [-100, -100], '--', color='gray')

    def to_dict(self):
        """
        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'n': self.n,
                'c': self.c,
                'column': self.column
            }
        }
