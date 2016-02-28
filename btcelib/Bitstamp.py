from btcelib.exchange import Exchange
import logging

log = logging.getLogger(__name__)


class Bitstamp(Exchange):
    """
    Bitstamp only has BTC_USD as a pair, hence the PAIR paramater does not need
    to be passed when querying the exchange.

    All functions calculating budgets or prices do NOT include trading fees.
    """
    def __init__(self):
        name = 'bitstamp.net'
        query_mask = '{_type}/{pair}'
        url = 'https://www.bitstamp.net/api/'
        pairs = {'BTCUSD': '',
                 'EURUSD': ''}

        types = {'orderbook': 'order_book',
                 'ticker':'ticker',
                 'trades': 'transactions',
                 'hourly_ticker': 'ticker_hour'
                 'conversion': 'eur_usd'}
        super(Bitstamp, self).__init__(url, query_mask, pairs, types, name)

    def ob(self, raw=False, file=None):
        """
        Returns the ticker as two lists; if file is passed, saves data as given
        file as well.
        If raw is True, return is a dict
        :param raw: bool
        :param file: str, filepath/name
        :return: list, list
        """
        if raw:
            return super(Bitstamp, self)._get_orderbook('BTCUSD', file)
        else:
            js = super(Bitstamp, self)._get_orderbook('BTCUSD', file)
            a = js['asks']
            b = js['bids']
            return a, b

    def trades(self, file=None):
        """
        Returns all recent trades as dict; if file is passed, saves data as
        given file as well.
        :param file: str, filepath/name
        :return: dict
        """
        return super(Bitstamp, self)._get_trades('BTCUSD', file)

    def ticker(self, file=None):
        """
        Returns the ticker as dict; if file is passed, saves data as given file
        as well.
        :param file: str, filepath/name
        :return: dict
        """
        return super(Bitstamp, self)._get_ticker('BTCUSD', file)

    def buy_budget(self, budget):
        """
        Return the maximum amount of currency purchasable with the given budget.
        :param budget: float/int
        :return: float
        """
        a, _ = self.ob()
        return super(Bitstamp, self)._trade_budget(budget, a)

    def sell_profit(self, profit):
        """
        Return total volume required to obtain the given profit margin.
        :profit: float/int
        :return: float
        """
        _, b = self.ob()
        return super(Bitstamp, self)._trade_budget(profit, b)

    def buy_vol(self, vol):
        """
        Return the total price for the given volume.
        :param vol: float/int
        :return: float
        """
        a, _ = self.ob()
        return super(Bitstamp, self)._trade_vol(vol, a)

    def sell_vol(self, vol):
        """
        Return total expected return for given volume of currency
        :param vol:
        :return:
        """
        _, b = self.ob()
        return super(Bitstamp, self)._trade_vol(vol, b)

