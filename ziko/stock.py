from ziko.transaction import Transaction


class Stock(object):
    def __init__(self, name):
        """

        :param name:
        :type name: str
        """
        self.name = name
        self.transactions = []
        self.shares = 0
        self.cost = 0

    @property
    def pairs(self):
        pairs = []
        current = []
        for t in self.transactions:
            current.append(t)
            if t.direction == Transaction.SELL:
                pairs.append(current)
                current = []

        return pairs

    def buy(self, timestamp, price, budget, cp=0.003):
        """

        :param timestamp:
        :type timestamp: int
        :param price: current price
        :type price: float
        :param budget:
        :type budget: float
        :param cp: commission percent
        :type cp: float
        :return: (int, float, float)
        """
        shares = int(budget // price)
        charge = shares * price
        commission = charge * cp

        if charge + commission > budget:
            share_reduction = (commission // price) + 1
            shares -= share_reduction
            charge = shares * price
            commission = charge * cp

        self.shares += shares
        self.cost += charge

        if shares > 0:
            self.transactions.append(
                Transaction(
                    timestamp=timestamp,
                    shares=shares,
                    price=price,
                    commission=commission,
                    direction=Transaction.BUY
                )
            )

        return shares, charge, commission

    def sell(self, timestamp, price, cp=0.003, tp=0.19):
        """

        :param timestamp:
        :type timestamp: int
        :param price: current price
        :type price: float
        :param cp: commission percent (0-1)
        :type cp: float
        :param tp: tax percent (0-1)
        :type tp: float
        :return:
        :rtype: (int, float, float)
        """
        shares = self.shares

        charge = shares * price
        commission = charge * cp

        tax = 0
        profit = charge - self.cost
        if profit > 0:
            tax = profit * tp

        if shares > 0:
            self.transactions.append(
                Transaction(
                    timestamp=timestamp,
                    shares=shares,
                    price=price,
                    commission=commission+tax,
                    direction=Transaction.SELL
                )
            )

        self.shares = 0
        self.cost = 0

        return shares, charge, commission + tax
