import ta

from ziko.indicators.base import BaseIndicator


class ChaikinMoneyFlow(BaseIndicator):
    NAME = 'ChaikinMoneyFlow'

    def __init__(self, period=20, column='close', *args, **kwargs):
        """
        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = 'cmf({},{})'.format(self.column, self.period)

    def calculate(self, data):
        """
        :param data:
        :type data: pandas.DataFrame
        """
        data[self.name] = ta.volume.chaikin_money_flow(data['high'], data['low'], data['close'], data['volume'], n=self.period)

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [0, 0], '--', color='lightgray')

    def to_dict(self):
        """
        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'column': self.column,
                'period': self.period
            }
        }
