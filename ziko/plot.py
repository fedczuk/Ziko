from matplotlib import pyplot as plt
import matplotlib.patches as patches

from ziko.transaction import Transaction


class Plot(object):
    COLORS = {
        Transaction.BUY: 'g',
        Transaction.SELL: 'r'
    }

    def __init__(self, name, rows=2, *args, **kwargs):
        """

        :param name:
        :type name: str
        """
        self.fig, self.ax = plt.subplots(
            nrows=rows, ncols=1,
            # gridspec_kw={'height_ratios': [2, 1]},
            sharex=True,
            *args, **kwargs
        )

        self.ax[0].title.set_text(name)

        self.ax[0].set_xlabel('Time')
        self.ax[0].set_ylabel('Price')

        self.ax[1].set_xlabel('Time')
        self.ax[1].set_ylabel('Volume')

    def __del__(self):
        plt.close(self.fig)

    def price(self, data, label=None, color='silver', *args, **kwargs):
        """

        :param data:
        :type data: pandas.DataFrame
        :param label:
        :type label: str
        :param color:
        :type color: str
        """
        data.plot(ax=self.ax[0], label=label, color=color, *args, **kwargs)

    def indicators(self, data, columns, ax, name, *args, **kwargs):
        """

        :param data:
        :type data: pandas.DataFrame
        :param columns:
        :type columns: list[str]
        """
        data[columns].plot(ax=ax, *args, **kwargs)
        ax.set_ylabel(name)

    def signals(self, signals):
        """

        :param signals:
        :type signals: list[ziko.strategies.event.Event]
        """
        ylim = self.ax[0].get_ylim()
        for s in signals:
            c = self.COLORS.get(s.direction)
            self.ax[0].plot([s.when] * 2, ylim, '-', color=c)

    def volume(self, data, *args, **kwargs):
        """

        :param data:
        :type data: pandas.DataFrame
        """
        data.plot(ax=self.ax[1], color='gray', *args, **kwargs)

    def _draw_balance(self, transactions, ax):
        """

        :param transactions:
        :type transactions: list[ziko.transaction.Transaction]
        """
        ylim = ax.get_ylim()

        pairs = []
        current = []
        for t in transactions:
            current.append(t)
            if t.direction == Transaction.SELL:
                pairs.append(current)
                current = []

        for buy, sell in pairs:
            color = 'honeydew' if sell.price > buy.price else 'mistyrose'

            width = sell.timestamp - buy.timestamp
            height = ylim[1] - ylim[0]

            rect = patches.Rectangle((buy.timestamp, ylim[0]), width, height, facecolor=color)
            ax.add_patch(rect)

    def transactions(self, transactions):
        """

        :param transactions:
        :type transactions: list[ziko.transaction.Transaction]
        """
        self._draw_balance(transactions, self.ax[0])

        for t in transactions:
            c = self.COLORS.get(t.direction)
            self.ax[0].plot(t.timestamp, t.price, marker='x', color=c)

    def transactions2(self, transactions, ax):
        """

        :param transactions:
        :type transactions: list[ziko.transaction.Transaction]
        """
        self._draw_balance(transactions, ax)

        # ylim = ax.get_ylim()
        # for t in transactions:
        #     c = self.COLORS.get(t.direction)
        #     ax.plot([t.timestamp] * 2, ylim, '--', color=c)

    def save(self, filename):
        """

        :param filename:
        :type filename: str
        """
        self.fig.savefig(filename)
