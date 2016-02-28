from btcelib.exchange import Exchange
import logging

log = logging.getLogger(__name__)

class Bitstamp(Exchange):
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

    def ob(self, pair='BTCUSD', raw=False, file=None):
        if raw:
            return super(Bitstamp, self)._get_orderbook(pair, file)
        else:
            js = super(Bitstamp, self)._get_orderbook(pair, file)
            for key in js['result']:
                a = js['asks']
                b = js['bids']
                return a, b

    def trades(self, pair, file=None):
        return super(Bitstamp, self)._get_trades(pair, file)

    def ticker(self, pair, file=None):
        return super(Bitstamp, self)._get_ticker(pair, file)


    def buy_budget(self, budget, pair):
        """
        Return the maximum amount of currency purchasable with the given budget.
        :param budget: float/int
        :param pair: str
        :return: float
        """
        a, _ = self.ob(pair)
        return super(Bitstamp, self)._trade_budget(budget, a)

    def sell_profit(self, profit, pair):
        """
        Return total volume required to obtain the given profit margin.
        :profit: float/int
        :pair: str
        :return: float
        """
        _, b = self.ob(pair)
        return super(Bitstamp, self)._trade_budget(profit, b)

    def buy_vol(self, vol, pair):
        """
        Return the total price for the given volume.
        :param vol: float/int
        :param pair: str
        :return: float
        """
        a, _ = self.ob(pair)
        return super(Bitstamp, self)._trade_vol(vol, a)

    def sell_vol(self, vol, pair):
        """
        Return total expected return for given volume of currency
        :param vol:
        :param pair:
        :return:
        """
        _, b = self.ob(pair)
        return super(Bitstamp, self)._trade_vol(vol, b)

