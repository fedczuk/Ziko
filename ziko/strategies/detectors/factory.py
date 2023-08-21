from ziko.strategies.detectors.crossing import CrossingDetector
from ziko.strategies.detectors.threshold import ThresholdDetector


class DetectorFactory(object):
    DETECTORS = {
        'CrossingDetector': CrossingDetector,
        'ThresholdDetector': ThresholdDetector
    }

    @staticmethod
    def make(setup):
        """

        :param setup:
        :type setup: dict
        :return:
        :rtype: ziko.strategies.detectors.base.BaseDetector
        """
        name = setup.get('name')
        detector = DetectorFactory.DETECTORS.get(name)
        return detector.from_dict(setup.get('params'))
