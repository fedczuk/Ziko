from ziko.indicators.base import BaseIndicator


class Partial(BaseIndicator):
    def __init__(self, column='close', parent=None, *args, **kwargs):
        """

        :param column:
        :type column: str
        """
        super().__init__(column, *args, **kwargs)
        self.parent = parent

    def calculate(self, data):
        if self.column not in data.columns:
            self.parent.calculate(data)
