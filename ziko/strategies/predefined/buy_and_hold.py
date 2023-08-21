from ziko.indicators.trend.ema import ExponentialMovingAverage as EMA
from ziko.strategies.event import Event
from ziko.strategies.predefined.simple_crossing import SimpleCrossingStrategy


class BuyAndHold(SimpleCrossingStrategy):
    def __init__(self):
        super().__init__(EMA(15), EMA(200))

    def events(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        :return:
        :rtype: list[ziko.strategies.event.Event]
        """
        events = super().events(data)
        if len(events) == 0:
            return []

        result = []
        for idx, e in enumerate(events):
            if e.direction == Event.BUY:
                result.append(e)
                break

        if events[-1].direction == Event.SELL:
            result.append(events[-1])

        return result
