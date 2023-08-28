from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class MovingAverage(BaseIndicator):
    NAME = 'MA'

    def __init__(self, period: int = 30, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = 'ma({},{})'.format(self.column, self.period)

    def calculate(self, data: DataFrame):
        data[self.name] = data[self.column].rolling(self.period).mean()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        plot.indicators(data, [self.column], axis, self.NAME, color='gray')

    def to_dict(self) -> dict:
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
