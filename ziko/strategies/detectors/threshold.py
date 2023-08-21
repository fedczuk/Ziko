from ziko.indicators.factory import IndicatorFactory
from ziko.strategies.detectors.base import BaseDetector


class ThresholdDetector(BaseDetector):
    ABOVE = 'above'
    ABOVE_EQUAL = 'above_equal'

    BELOW = 'below'
    BELOW_EQUAL = 'below_equal'

    def __init__(self, indicator, direction, value):
        """

        :param indicator:
        :type indicator: ziko.indicators.base.BaseIndicator
        :param direction:
        :type direction: str
        :param value:
        :type value: float
        """
        self.indicator = indicator
        self.direction = direction
        self.value = value

    @property
    def indicators(self):
        """

        :return:
        :rtype: set[ziko.indicators.base.BaseIndicator]
        """
        return {self.indicator}

    def signals(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        :return:
        :rtype: pandas.Series
        """
        if self.direction == self.ABOVE:
            return data[self.indicator.name] > self.value
        elif self.direction == self.ABOVE_EQUAL:
            return data[self.indicator.name] >= self.value
        elif self.direction == self.BELOW:
            return data[self.indicator.name] < self.value
        elif self.direction == self.BELOW_EQUAL:
            return data[self.indicator.name] <= self.value

    def to_dict(self):
        """

        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'indicator': self.indicator.to_dict(),
                'direction': self.direction,
                'value': self.value,
            }
        }

    @classmethod
    def from_dict(cls, params):
        """

        :param params:
        :type params: dict
        :return:
        :rtype: ThresholdDetector
        """
        params['indicator'] = IndicatorFactory.make(params.get('indicator'))
        return cls(**params)
