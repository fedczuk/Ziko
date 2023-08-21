import ta

from ziko.indicators.base import BaseIndicator


class VolumePriceTrend(BaseIndicator):
    NAME = 'VolumePriceTrend'

    def __init__(self, column='close', *args, **kwargs):
        """
        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.name = 'vpt({})'.format(self.column)

    def calculate(self, data):
        """
        :param data:
        :type data: pandas.DataFrame
        """
        data[self.name] = ta.volume.volume_price_trend(data['close'], data['volume'])

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
