import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator

from ziko.indicators.column import Column


class BollingerBands(BaseIndicator):
    NAME = 'BB'

    def __init__(self, period: int = 20, stddev: int = 2, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.period = period
        self.stddev = stddev
        self.name = None

        self._high_band_col = 'bh({},{}-{})'.format(self.column, self.period, self.stddev)
        self._avg_col = 'ba({},{}-{})'.format(self.column, self.period, self.stddev)
        self._low_band_col = 'bl({},{}-{})'.format(self.column, self.period, self.stddev)

    @property
    def high_band(self) -> Column:
        return Column(self._high_band_col)

    @property
    def avg(self) -> Column:
        return Column(self._avg_col)

    @property
    def low_band(self) -> Column:
        return Column(self._low_band_col)

    def calculate(self, data: DataFrame):
        bb = ta.volatility.BollingerBands(data[self.column], n=self.period, ndev=self.stddev)
        data[self._avg_col] = bb.bollinger_mavg()
        data[self._high_band_col] = bb.bollinger_hband()
        data[self._low_band_col] = bb.bollinger_lband()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.column], axis, self.NAME, color='lightgray')
        plot.indicators(data, [self._avg_col, self._high_band_col, self._low_band_col], axis, self.NAME)

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'period': self.period,
                'stddev': self.stddev,
                'column': self.column
            }
        }
