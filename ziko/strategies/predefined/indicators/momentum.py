from ziko.indicators.momentum.ao import AwesomeOscillator
from ziko.indicators.momentum.roc import RateOfChange
from ziko.indicators.momentum.tsi import TrueStrengthIndex
from ziko.strategies.predefined.symmetric_threshold import SymmetricThresholdStrategy


class TrueStrengthIndexStrategy(SymmetricThresholdStrategy):
    def __init__(self, threshold=0):
        tsi = TrueStrengthIndex()
        super().__init__(tsi, threshold)


class AwesomeOscillatorStrategy(SymmetricThresholdStrategy):
    def __init__(self, threshold=0):
        ao = AwesomeOscillator()
        super().__init__(ao, threshold)


class RateOfChangeStrategy(SymmetricThresholdStrategy):
    def __init__(self, threshold=0):
        roc = RateOfChange()
        super().__init__(roc, threshold)
