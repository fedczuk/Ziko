from copy import deepcopy

from ziko.strategies.operators import OperatorFactory
from ziko.strategies.event import Event


class Strategy(object):
    def __init__(self, buy, sell):
        """

        :param buy:
        :type buy: ziko.strategies.operators.BaseOperator
        :param sell:
        :type sell: ziko.strategies.operators.BaseOperator
        """
        self.buy = buy
        self.sell = sell

    @property
    def indicators(self):
        """

        :return:
        :rtype: set[ziko.indicators.base.BaseIndicator]
        """
        result = set()
        for s in self.buy.detectors + self.sell.detectors:
            result |= s.indicators

        return result

    def _calculate_indicators(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        :return:
        """
        for i in self.indicators:
            i.calculate(data)

    def _generate_events(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        :return:
        :rtype: list[ziko.strategies.event.Event]
        """
        signals = []
        for idx in self.buy.signals(data):
            signals.append(Event(Event.BUY, idx, data.loc[idx]['close']))

        for idx in self.sell.signals(data):
            signals.append(Event(Event.SELL, idx, data.loc[idx]['close']))

        return sorted(signals, key=lambda x: (x.when, x.direction))

    def events(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        :return:
        :rtype: list[ziko.strategies.event.Event]
        """
        self._calculate_indicators(data)
        return self._generate_events(data)

    def merge(self, strategy):
        buy = deepcopy(self.buy)
        sell = deepcopy(self.sell)

        buy.detectors.extend(strategy.buy.detectors)
        sell.detectors.extend(strategy.sell.detectors)

        return Strategy(buy, sell)

    def to_dict(self):
        """

        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'buy': self.buy.to_dict(),
                'sell': self.sell.to_dict(),
            }
        }

    @classmethod
    def from_dict(cls, params):
        """

        :param params:
        :type params: dict
        :return:
        :rtype: Strategy
        """
        buy = OperatorFactory.make(params['buy'])
        sell = OperatorFactory.make(params['sell'])
        return cls(buy, sell)
