from ziko.portfolio import Portfolio
from ziko.strategies.event import Event


class Validation(object):
    def __init__(self, strategy):
        """

        :param strategy:
        :type strategy: ziko.strategies.strategy.Strategy
        """
        self.strategy = strategy

    def test(self, quote, budget=10000):
        """

        :param quote:
        :type quote: ziko.quote.Quote
        :param budget:
        :type budget: float
        :return:
        :rtype: (ziko.portfolio.Portfolio, list[ziko.strategies.event.Event])
        """
        portfolio = Portfolio(budget)
        events = self.strategy.events(quote.data)

        for s in events:
            if s.direction == Event.BUY:
                portfolio.buy(quote.name, s.when, s.price, portfolio.current_budget)
            elif s.direction == Event.SELL:
                portfolio.sell(quote.name, s.when, s.price)

        last_quote = quote.data.tail(1).iloc[0]
        portfolio.sell(quote.name, last_quote.name, float(last_quote['close']))

        return portfolio, events
