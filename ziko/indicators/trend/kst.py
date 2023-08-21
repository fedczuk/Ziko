import ta

from ziko.indicators.base import BaseIndicator
from ziko.indicators.partial import Partial


class KSTIndicator(BaseIndicator):
    NAME = 'KST'

    def __init__(self, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15, nsig=9, column='close', *args, **kwargs):
        """
        :param period:
        :type period: int
        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.nsig = nsig
        self.name = None

        self._kst_col = 'kst({},{}-{}-{})'.format(
            self.column,
            self.r1, self.r2, self.r3, self.r4,
            self.n1, self.n2, self.n3, self.n4,
            self.nsig
        )
        self._kst_diff_col = 'kst_diff({},{}-{}-{})'.format(
            self.column,
            self.r1, self.r2, self.r3, self.r4,
            self.n1, self.n2, self.n3, self.n4,
            self.nsig
        )
        self._kst_sig_col = 'kst_sig({},{}-{}-{})'.format(
            self.column,
            self.r1, self.r2, self.r3, self.r4,
            self.n1, self.n2, self.n3, self.n4,
            self.nsig
        )

    @property
    def kst(self):
        return Partial(self._kst_col, self)

    @property
    def diff(self):
        return Partial(self._kst_diff_col, self)

    @property
    def sig(self):
        return Partial(self._kst_sig_col, self)

    def calculate(self, data):
        """
        :param data:
        :type data: pandas.DataFrame
        """
        indicator = ta.trend.KSTIndicator(
            data['close'],
            r1=self.r1, r2=self.r2, r3=self.r3, r4=self.r4,
            n1=self.n1, n2=self.n2, n3=self.n3, n4=self.n4,
            nsig=self.nsig
        )

        data[self._kst_col] = indicator.kst()
        data[self._kst_diff_col] = indicator.kst_diff()
        data[self._kst_sig_col] = indicator.kst_sig()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self._kst_col, self._kst_sig_col], axis, self.NAME)

    def to_dict(self):
        """
        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'r1': self.r1,
                'r2': self.r2,
                'r3': self.r3,
                'r4': self.r4,
                'n1': self.n1,
                'n2': self.n2,
                'n3': self.n3,
                'n4': self.n4,
                'nsig': self.nsig,
                'column': self.column
            }
        }
