class BaseIndicator(object):
    NAME = None

    def __init__(self, column='close', *args, **kwargs):
        """

        :param column:
        :type column: str
        """
        self.column = column
        self.name = column

    def calculate(self, data):
        """

        :param data:
        :type data: pandas.DataFrame
        :return:
        """
        raise NotImplementedError()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)

    def to_dict(self):
        """

        :return:
        :rtype: dict
        """
        return {
            'name': self.__class__.__name__,
            'params': {
                'column': self.column
            }
        }

    @classmethod
    def from_dict(cls, params):
        """

        :param params:
        :type params: dict
        :return:
        :rtype: BaseIndicator
        """
        return cls(**params)
