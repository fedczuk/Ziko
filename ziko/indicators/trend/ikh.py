import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator
from ziko.indicators.column import Column


class IchimokuIndicator(BaseIndicator):
    NAME = 'IchimokuIndicator'

    def __init__(self, n1: int = 9, n2: int = 26, n3: int = 52, visual: bool = False, column: str = 'close', *args,
                 **kwargs):
        super().__init__(column, *args, **kwargs)
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.visual = visual
        self.name = None

        self._ikh_a_col = 'ikha({},{}-{}-{})'.format(self.column, self.n1, self.n2, self.n3)
        self._ikh_b_col = 'ikhb({},{}-{}-{})'.format(self.column, self.n1, self.n2, self.n3)

    @property
    def a(self) -> Column:
        return Column(self._ikh_a_col)

    @property
    def b(self) -> Column:
        return Column(self._ikh_b_col)

    def calculate(self, data: DataFrame):
        indicator = ta.trend.IchimokuIndicator(
            data['high'], data['low'], n1=self.n1, n2=self.n2, n3=self.n3, visual=self.visual
        )

        data[self._ikh_a_col] = indicator.ichimoku_a()
        data[self._ikh_b_col] = indicator.ichimoku_b()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self._ikh_a_col, self._ikh_b_col], axis, self.NAME)
        plot.indicators(data, [self.column], axis, self.NAME, color='gray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'n1': self.n1,
                'n2': self.n2,
                'n3': self.n3,
                'column': self.column
            }
        }
