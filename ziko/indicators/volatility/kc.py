import ta

from ziko.indicators.base import BaseIndicator

from ziko.indicators.column import Column


class KeltnerChannel(BaseIndicator):
    NAME = 'KeltnerChannel'

    def __init__(self, period=14, column='close', *args, **kwargs):
        """

        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.name = None

        self._high_band_col = 'kch({},{})'.format(self.column, self.period)
        self._avg_col = 'kca({},{})'.format(self.column, self.period)
        self._low_band_col = 'kcl({},{})'.format(self.column, self.period)

    @property
    def high_band(self):
        return Column(self._high_band_col)

    @property
    def avg(self):
        return Column(self._avg_col)

    @property
    def low_band(self):
        return Column(self._low_band_col)

    def calculate(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        """
        kc = ta.volatility.KeltnerChannel(data['high'], data['low'], data['close'], n=self.period)
        data[self._avg_col] = kc.keltner_channel_central()
        data[self._high_band_col] = kc.keltner_channel_hband()
        data[self._low_band_col] = kc.keltner_channel_lband()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.column], axis, self.NAME, color='lightgray')
        plot.indicators(data, [self._avg_col, self._high_band_col, self._low_band_col], axis, self.NAME)

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
