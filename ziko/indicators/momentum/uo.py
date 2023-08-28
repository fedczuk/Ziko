import ta
from pandas import DataFrame

from ziko.indicators.base import BaseIndicator


class UltimateOscillator(BaseIndicator):
    NAME = 'UltimateOscillator'

    def __init__(self, sp: int = 7, mp: int = 14, lp: int = 28, ws: int = 4.0, wm: int = 2.0, wl: int = 1.0,
                 column: str = 'close', *args, **kwargs):
        super().__init__(column, *args, **kwargs)
        self.sp = sp
        self.mp = mp
        self.lp = lp
        self.ws = ws
        self.wm = wm
        self.wl = wl

        self.name = 'uo({},{}-{}-{}-{}-{}-{})'.format(
            self.column,
            self.sp, self.mp, self.lp,
            self.ws, self.wm, self.wl
        )

    def calculate(self, data: DataFrame):
        data[self.name] = ta.momentum.uo(
            data['high'], data['low'], data['close'],
            s=self.sp, m=self.mp, len=self.lp, ws=self.ws, wm=self.wm, wl=self.wl
        )

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)
        axis.plot([data.index.min(), data.index.max()], [70, 70], '--', color='gray')
        axis.plot([data.index.min(), data.index.max()], [30, 30], '--', color='gray')

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'sp': self.sp,
                'mp': self.mp,
                'lp': self.lp,
                'ws': self.ws,
                'wm': self.wm,
                'wl': self.wl,
                'column': self.column
            }
        }
