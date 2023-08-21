from ziko.indicators.factory import IndicatorFactory
from ziko.strategies.detectors.base import BaseDetector


class CrossingDetector(BaseDetector):
    def __init__(self, lower, upper):
        """

        :param lower:
        :type lower: ziko.indicators.base.BaseIndicator
        :param upper:
        :type upper: ziko.indicators.base.BaseIndicator
        """
        self.lower = lower
        self.upper = upper

    @property
    def indicators(self):
        """

        :return:
        :rtype: set[ziko.indicators.base.BaseIndicator]
        """
        return {self.lower, self.upper}

    def signals(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        :return:
        :rtype: pandas.Series
        """
        indicators = data[[self.lower.name, self.upper.name]]
        return indicators[self.lower.name] > indicators[self.upper.name]

    def to_dict(self):
        """

        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'lower': self.lower.to_dict(),
                'upper': self.upper.to_dict(),
            }
        }

    @classmethod
    def from_dict(cls, params):
        """

        :param params:
        :type params: dict
        :return:
        :rtype: CrossingDetector
        """
        lower = IndicatorFactory.make(params.get('lower'))
        upper = IndicatorFactory.make(params.get('upper'))
        return cls(lower, upper)
