from ziko.stock import Stock


class Portfolio(object):
    def __init__(self, budget):
        """

        :param budget: initial budget
        :type budget: float
        """
        self.initial_budget = budget
        self.current_budget = budget
        self.stocks = {}

    @property
    def current(self):
        return [s for s in self.stocks if self.stocks[s].shares > 0]

    def buy(self, stock, when, price, budget):
        """

        :param stock:
        :type stock: str
        :param when:
        :type when: int
        :param price:
        :type price: float
        :param budget:
        :type budget: float
        :return: True when transaction succeeded, False otherwise.
        :rtype: bool
        """
        if budget > self.current_budget:
            budget = self.current_budget

        s = self.stocks.get(stock, Stock(name=stock))
        # don't allow to buy more stocks
        if s.shares > 0:
            return False

        shares, charge, commission = s.buy(when, price, budget)
        if shares > 0:
            self.current_budget -= (charge + commission)
            self.stocks[stock] = s

            return True

        return False

    def sell(self, stock, when, price):
        """

        :param stock:
        :type stock: str
        :param when:
        :type when: int
        :param price:
        :type price: float
        :return: True when transaction succeeded, False otherwise.
        :rtype: bool
        """
        s = self.stocks.get(stock)
        if s is None:
            return False

        # don't allow to sell security you don't own
        if s.shares == 0:
            return False

        shares, charge, commission = s.sell(when, price, tp=0)
        self.current_budget += (charge - commission)

        self.stocks[stock] = s
        return (charge - commission)
