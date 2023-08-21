class BaseDetector(object):
    @property
    def indicators(self):
        """

        :return:
        :rtype: set[ziko.indicators.base.BaseIndicator]
        """
        raise NotImplementedError()

    def signals(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        :return:
        :rtype: pandas.Series
        """
        raise NotImplementedError()

    def to_dict(self):
        raise NotImplementedError()

    @classmethod
    def from_dict(cls, params):
        raise NotImplementedError()
