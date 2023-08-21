from ziko.indicators.base import BaseIndicator


class Column(BaseIndicator):
    def __init__(self, column='close', *args, **kwargs):
        """

        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)

    def calculate(self, data):
        pass
