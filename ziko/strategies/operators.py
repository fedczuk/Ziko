import pandas as pd

from ziko.strategies.detectors.factory import DetectorFactory


class BaseOperator(object):
    def __init__(self, detectors):
        """

        :param detectors:
        :type detectors: list[ziko.strategies.detectors.base.BaseDetector]
        """
        self.detectors = detectors

    def _aggregate(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        :return:
        :rtype: pandas.DataFrame
        """
        signals = []
        for i, s in enumerate(self.detectors):
            signal = s.signals(data)
            signal.name = str(i)
            signals.append(signal)

        return pd.concat(signals, axis=1)

    def _operator(self, dfs):
        """

        :param dfs:
        :type dfs: pandas.DataFrame
        :return:
        :rtype: pandas.Series
        """
        raise NotImplementedError

    def signals(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        :return:
        :rtype: list[int]
        """
        signals = self._aggregate(data)

        dfs = pd.DataFrame(signals)
        dfs['signal'] = self._operator(dfs)

        dfs['signal'] = dfs['signal'].astype(int)
        dfs['signal'] = dfs['signal'].diff()

        return list(dfs[dfs['signal'] >= 1].index)

    def to_dict(self):
        """

        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'detectors': [s.to_dict() for s in self.detectors]
            }
        }

    @classmethod
    def from_dict(cls, params):
        """

        :param params:
        :type params: dict
        :return:
        :rtype: BaseOperator
        """
        detectors = []
        for s in params['detectors']:
            detectors.append(DetectorFactory.make(s))

        return cls(detectors)


class Or(BaseOperator):
    def _operator(self, dfs):
        """

        :param dfs:
        :type dfs: pandas.DataFrame
        :return:
        :rtype: pandas.Series
        """
        return dfs.any(axis=1)


class And(BaseOperator):
    def _operator(self, dfs):
        """

        :param dfs:
        :type dfs: pandas.DataFrame
        :return:
        :rtype: pandas.Series
        """
        return dfs.all(axis=1)


class OperatorFactory(object):
    OPERATORS = {
        'Or': Or,
        'And': And
    }

    @staticmethod
    def make(setup):
        """

        :param setup:
        :type setup: dict
        :return:
        :rtype: BaseOperator
        """
        name = setup.get('name')
        operator = OperatorFactory.OPERATORS.get(name)
        return operator.from_dict(setup.get('params'))
