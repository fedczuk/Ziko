from ziko.indicators.trend.adx import AverageDirectionalMovement
from ziko.indicators.trend.ai import AroonIndicator
from ziko.indicators.trend.ema import ExponentialMovingAverage as EMA
from ziko.indicators.trend.ma import MovingAverage as MA
from ziko.indicators.trend.kst import KSTIndicator
from ziko.indicators.trend.vi import VortexIndicator
from ziko.strategies.predefined.simple_crossing import SimpleCrossingStrategy
from ziko.strategies.predefined.symmetric_threshold import SymmetricThresholdStrategy


class MAStrategy(SimpleCrossingStrategy):
    def __init__(self, fp=15, sp=200):
        fast = MA(fp)
        slow = MA(sp)

        super().__init__(fast, slow)


class EMAStrategy(SimpleCrossingStrategy):
    def __init__(self, fp=15, sp=200):
        fast = EMA(fp)
        slow = EMA(sp)

        super().__init__(fast, slow)


class AroonStrategy(SimpleCrossingStrategy):
    def __init__(self, p=25):
        ai = AroonIndicator(p)
        super().__init__(ai.ai_up, ai.ai_down)


class KSTStrategy(SimpleCrossingStrategy):
    def __init__(self):
        kst = KSTIndicator()
        super().__init__(kst.kst, kst.sig)


class VortexStrategy(SimpleCrossingStrategy):
    def __init__(self, p=14):
        vi = VortexIndicator(p)
        super().__init__(vi.pos, vi.neg)


class ADXStrategy(SymmetricThresholdStrategy):
    def __init__(self, threshold=25):
        adx = AverageDirectionalMovement()
        super().__init__(adx.adx, threshold)
