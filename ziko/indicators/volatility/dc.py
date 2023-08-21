import ta

from ziko.indicators.base import BaseIndicator

from ziko.indicators.column import Column


class DonchianChannel(BaseIndicator):
    NAME = 'DonchianChannel'

    def __init__(self, period=20, stddev=2, column='close', *args, **kwargs):
        """

        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.stddev = stddev
        self.name = None

        self._high_band_col = 'dch({},{}-{}'.format(self.column, self.period, self.stddev)
        self._low_band_col = 'dcl({},{}-{}'.format(self.column, self.period, self.stddev)

    @property
    def high_band(self):
        return Column(self._high_band_col)

    @property
    def low_band(self):
        return Column(self._low_band_col)

    def calculate(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        """
        dc = ta.volatility.DonchianChannel(data[self.column], n=self.period)
        data[self._high_band_col] = dc.donchian_channel_hband()
        data[self._low_band_col] = dc.donchian_channel_lband()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.column], axis, self.NAME, color='lightgray')
        plot.indicators(data, [self._high_band_col, self._low_band_col], axis, self.NAME)

    def to_dict(self):
        """

        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'period': self.period,
                'stddev': self.stddev,
                'column': self.column
            }
        }
