from ziko.indicators.volume.cmf import ChaikinMoneyFlow
from ziko.strategies.predefined.symmetric_threshold import SymmetricThresholdStrategy


class CMFStrategy(SymmetricThresholdStrategy):
    def __init__(self):
        cmf = ChaikinMoneyFlow()
        super().__init__(cmf, 0)