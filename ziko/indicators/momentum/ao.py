import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class AwesomeOscillator(BaseIndicator):
    NAME = 'AwesomeOscillator'

    def __init__(self, sp: int = 5, lp: int = 34, column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.sp = sp
        self.lp = lp
        self.name = 'ao({},{}-{})'.format(self.column, self.sp, self.lp)

    def calculate(self, data: DataFrame):
        data[self.name] = ta.momentum.ao(
            data['high'], data['low'], s=self.sp, len=self.lp
        )

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [0, 0], '--', color='gray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'sp': self.sp,
                'lp': self.lp,
                'column': self.column
            }
        }
