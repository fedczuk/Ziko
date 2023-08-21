import ta

from ziko.indicators.base import BaseIndicator


class OnBalanceVolume(BaseIndicator):
    NAME = 'OBV'

    def __init__(self, column='close', *args, **kwargs):
        """
        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.name = 'obv({})'.format(self.column)

    def calculate(self, data):
        """
        :param data:
        :type data: pandas.DataFrame
        """
        data[self.name] = ta.volume.on_balance_volume(data['close'], data['volume'])

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
                'column': self.column
            }
        }
