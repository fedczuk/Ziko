from pandas import DataFrame


class BaseIndicator:
    NAME = None

    def __init__(self, column: str = 'close', *args, **kwargs):
        self.column = column
        self.name = column

    def calculate(self, data: DataFrame):
        raise NotImplementedError()

    def plot(self, plot, axis, data):
        plot.indicators(data, [self.name], axis, self.NAME)

    def to_dict(self) -> dict:
        return {
            'name': self.__class__.__name__,
            'params': {
                'column': self.column
            }
        }

    @classmethod
    def from_dict(cls, params: dict):
        return cls(**params)
