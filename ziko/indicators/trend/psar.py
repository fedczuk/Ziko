import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator
from ziko.indicators.column import Column


class PSARIndicator(BaseIndicator):
    NAME = 'PSAR'

    def __init__(self, step: float = 0.02, max_step: float = 0.2, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.step = step
        self.max_step = max_step
        self.name = None

        self._psar_col = 'psar({},{}-{})'.format(self.column, self.step, self.max_step)

        self._psar_down_col = 'psar_down({},{}-{})'.format(self.column, self.step, self.max_step)
        self._psar_down_indicator_col = 'psar_down_i({},{}-{})'.format(self.column, self.step, self.max_step)

        self._psar_up_col = 'psar_up({},{}-{})'.format(self.column, self.step, self.max_step)
        self._psar_up_indicator_col = 'psar_up_i({},{}-{})'.format(self.column, self.step, self.max_step)

    @property
    def psar(self) -> Column:
        return Column(self._psar_col)

    @property
    def down(self) -> Column:
        return Column(self._psar_down_col)

    @property
    def down_indicator(self) -> Column:
        return Column(self._psar_down_indicator_col)

    @property
    def up(self) -> Column:
        return Column(self._psar_up_col)

    @property
    def up_indicator(self) -> Column:
        return Column(self._psar_up_indicator_col)

    def calculate(self, data: DataFrame):
        indicator = ta.trend.PSARIndicator(
            data['high'], data['low'], data['close'],
            step=self.step, max_step=self.max_step
        )
        data[self._psar_col] = indicator.psar()
        data[self._psar_down_col] = indicator.psar_down()
        data[self._psar_down_indicator_col] = indicator.psar_down_indicator()
        data[self._psar_up_col] = indicator.psar_up()
        data[self._psar_up_indicator_col] = indicator.psar_up_indicator()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.column], axis, self.NAME, color='lightgray')

        lines = [
            self._psar_col,
            self._psar_down_col,
            self._psar_up_col,
        ]
        plot.indicators(data, lines, axis, self.NAME)

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'step': self.step,
                'max_step': self.max_step,
                'column': self.column
            }
        }
