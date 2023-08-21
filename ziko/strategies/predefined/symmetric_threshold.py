from ziko.strategies.detectors.threshold import ThresholdDetector
from ziko.strategies.operators import And
from ziko.strategies.strategy import Strategy


class SymmetricThresholdStrategy(Strategy):
    def __init__(self, indicator, threshold):
        """

        :param indicator:
        :type indicator: ziko.indicators.base.BaseIndicator
        """
        buy = ThresholdDetector(indicator, ThresholdDetector.ABOVE, threshold)
        sell = ThresholdDetector(indicator, ThresholdDetector.BELOW, threshold)
        super().__init__(And([buy]), And([sell]))
