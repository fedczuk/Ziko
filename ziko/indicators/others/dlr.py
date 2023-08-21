import ta

from ziko.indicators.base import BaseIndicator


class DailyLogReturn(BaseIndicator):
    NAME = 'DailyLogReturn'

    def __init__(self, column='close', *args, **kwargs):
        """
        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.name = 'dlr({})'.format(self.column)

    def calculate(self, data):
        """
        :param data:
        :type data: pandas.DataFrame
        """
        data[self.name] = ta.others.daily_log_return(data['close'])

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
