class Transaction(object):
    BUY = 'buy'
    SELL = 'sell'

    def __init__(self, timestamp, shares, price, commission, direction):
        """

        :param timestamp:
        :type timestamp: int
        :param shares:
        :type shares: int
        :param price:
        :type price: float
        :param commission:
        :type commission: float
        :param direction:
        :type direction: str
        """
        self.timestamp = timestamp
        self.shares = shares
        self.price = price
        self.commission = commission
        self.direction = direction

    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'shares': self.shares,
            'price': self.price,
            'commission': self.commission,
            'direction': self.direction
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return '{} {} P: {} S: {} C: {}'.format(
            self.timestamp, self.direction,
            round(self.price, 2), round(self.shares, 2), round(self.commission, 2)
        )


