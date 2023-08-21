from ziko.strategies.detectors.crossing import CrossingDetector
from ziko.strategies.operators import And
from ziko.strategies.strategy import Strategy


class SimpleCrossingStrategy(Strategy):
    def __init__(self, fast, slow):
        """

        :param fast:
        :type fast: ziko.indicators.base.BaseIndicator
        :param slow:
        :type slow: ziko.indicators.base.BaseIndicator
        """
        buy = CrossingDetector(fast, slow)
        sell = CrossingDetector(slow, fast)
        super().__init__(And([buy]), And([sell]))
