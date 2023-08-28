from ziko.indicators.column import Column
from ziko.indicators.momentum.ao import AwesomeOscillator
from ziko.indicators.momentum.kama import KaufmanAdaptiveMovingAverage
from ziko.indicators.momentum.mfi import MoneyFlowIndex
from ziko.indicators.momentum.roc import RateOfChange
from ziko.indicators.momentum.rsi import RelativeStrengthIndex
from ziko.indicators.momentum.stoch import StochasticOscillator
from ziko.indicators.momentum.tsi import TrueStrengthIndex
from ziko.indicators.momentum.uo import UltimateOscillator
from ziko.indicators.momentum.wr import WilliamsR
from ziko.indicators.others.cr import CumulativeReturn
from ziko.indicators.others.dlr import DailyLogReturn
from ziko.indicators.others.dr import DailyReturn
from ziko.indicators.trend.adx import AverageDirectionalMovement
from ziko.indicators.trend.ai import AroonIndicator
from ziko.indicators.trend.cci import CommodityChannelIndex
from ziko.indicators.trend.dpo import DetrendedPriceOscillator
from ziko.indicators.trend.ema import ExponentialMovingAverage
from ziko.indicators.trend.ikh import IchimokuIndicator
from ziko.indicators.trend.kst import KSTIndicator
from ziko.indicators.trend.ma import MovingAverage
from ziko.indicators.trend.macd import MovingAverageConvergenceDivergence
from ziko.indicators.trend.mi import MassIndex
from ziko.indicators.trend.psar import PSARIndicator
from ziko.indicators.trend.trix import Trix
from ziko.indicators.trend.vi import VortexIndicator
from ziko.indicators.volatility.atr import AverageTrueRange
from ziko.indicators.volatility.bb import BollingerBands
from ziko.indicators.volatility.dc import DonchianChannel
from ziko.indicators.volatility.kc import KeltnerChannel
from ziko.indicators.volume.adi import AccumulationDistributionIndex
from ziko.indicators.volume.cmf import ChaikinMoneyFlow
from ziko.indicators.volume.eom import EaseOfMovement
from ziko.indicators.volume.fi import ForceIndex
from ziko.indicators.volume.nvi import NegativeVolumeIndex
from ziko.indicators.volume.obv import OnBalanceVolume
from ziko.indicators.volume.vpt import VolumePriceTrend


class IndicatorFactory(object):
    INDICATORS = {
        'AwesomeOscillator': AwesomeOscillator,
        'KaufmanAdaptiveMovingAverage': KaufmanAdaptiveMovingAverage,
        'MoneyFlowIndex': MoneyFlowIndex,
        'RateOfChange': RateOfChange,
        'RelativeStrengthIndex': RelativeStrengthIndex,
        'StochasticOscillator': StochasticOscillator,
        'TrueStrengthIndex': TrueStrengthIndex,
        'UltimateOscillator': UltimateOscillator,
        'WilliamsR': WilliamsR,
        'CumulativeReturn': CumulativeReturn,
        'DailyLogReturn': DailyLogReturn,
        'DailyReturn': DailyReturn,
        'AverageDirectionalMovement': AverageDirectionalMovement,
        'AroonIndicator': AroonIndicator,
        'CommodityChannelIndex': CommodityChannelIndex,
        'DetrendedPriceOscillator': DetrendedPriceOscillator,
        'IchimokuIndicator': IchimokuIndicator,
        'KSTIndicator': KSTIndicator,
        'MovingAverage': MovingAverage,
        'MovingAverageConvergenceDivergence': MovingAverageConvergenceDivergence,
        'MassIndex': MassIndex,
        'PSARIndicator': PSARIndicator,
        'Trix': Trix,
        'VortexIndicator': VortexIndicator,
        'ExponentialMovingAverage': ExponentialMovingAverage,
        'AverageTrueRange': AverageTrueRange,
        'BollingerBands': BollingerBands,
        'DonchianChannel': DonchianChannel,
        'KeltnerChannel': KeltnerChannel,
        'AccumulationDistributionIndex': AccumulationDistributionIndex,
        'ChaikinMoneyFlow': ChaikinMoneyFlow,
        'EaseOfMovement': EaseOfMovement,
        'ForceIndex': ForceIndex,
        'NegativeVolumeIndex': NegativeVolumeIndex,
        'OnBalanceVolume': OnBalanceVolume,
        'VolumePriceTrend': VolumePriceTrend,
        'Column': Column,
    }

    @staticmethod
    def make(setup: dict):
        name = setup.get('name')
        indicator = IndicatorFactory.INDICATORS.get(name)
        return indicator.from_dict(setup.get('params'))
