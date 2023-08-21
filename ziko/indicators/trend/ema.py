from ziko.indicators.base import BaseIndicator


class ExponentialMovingAverage(BaseIndicator):
    NAME = 'EMA'

    def __init__(self, period=30, column='close', *args, **kwargs):
        """
        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = 'ema({},{})'.format(self.column, self.period)

    def calculate(self, data):
        """
        :param data:
        :type data: pandas.DataFrame
        """
        data[self.name] = data[self.column].ewm(span=self.period).mean()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        plot.indicators(data, [self.column], axis, self.NAME, color='lightgray')

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
