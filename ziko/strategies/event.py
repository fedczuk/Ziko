class Event(object):
    BUY = 'buy'
    SELL = 'sell'

    def __init__(self, direction, when, price):
        """

        :param direction:
        :type direction: str
        :param when:
        :type when: int
        :param price:
        :type price: float
        """
        self.direction = direction
        self.when = when
        self.price = price
