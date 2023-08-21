class Performance(object):
    def __init__(self, portfolio):
        self.portfolio = portfolio

    @property
    def rate_of_return(self):
        """

        :return:
        :rtype: float
        """
        ratio = self.portfolio.current_budget / self.portfolio.initial_budget
        return (ratio * 100) - 100
