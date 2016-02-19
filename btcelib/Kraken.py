from btcelib.exchange import Exchange
import logging

log = logging.getLogger(__name__)

class Kraken(Exchange):
    def __init__(self):
        name = 'Kraken.com'
        query_mask = '{_type}?pair={pair}'
        url = 'https://api.kraken.com/0/public/'
        pairs = {'XBTEUR': 'XBTEUR',
                 'XBTUSD': 'XBTUSD',
                 'XBTCAD': 'XBTCAD',
                 'XBTGBP': 'XBTGBP',
                 'XBTJPY': 'XBTJPY',
                 'XBTLTC': 'XBTLTC',
                 'XBTNMC': 'XBTNMC',
                 'XBTXDG': 'XBTXDG',
                 'XBTXLM': 'XBTXLM',
                 'XBTXRP': 'XBTXRP',
                 'LTCEUR': 'LTCEUR',
                 'LTCUSD': 'LTCUSD',
                 'ETHEUR': 'ETHEUR',
                 'ETHUSD': 'ETHUSD',
                 'ETHCAD': 'ETHCAD',
                 'ETHGBP': 'ETHGBP',
                 'ETHJPY': 'ETHJPY',
                 'ETHXBT': 'ETHXBT'}
        types = {'orderbook': 'Depth',
                 'ticker':'Ticker',
                 'trades': 'Trades',
                 'OHLC': 'OHLC',
                 'spread': 'spread'}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

    def ob(self, pair, raw=False, file=None):
        """
        Returns two lists, asks & bids. If raw is True, we'll return the raw
        json query.
        :param pair: str
        :param raw: bool
        :return: list, list
        """
        if raw:
            return super(Kraken, self)._get_orderbook(pair, file)
        else:
            js = super(Kraken, self)._get_orderbook(pair, file)
            for key in js['result']:
                a = js['result'][key]['asks']
                b = js['result'][key]['bids']
                return a, b

    def trades(self, pair, raw=False, file=None):
        """
        Returns list of trades from JSON query. If raw is True, we'll return the
        raw json query.
        :param pair: str
        :param raw: bool
        :return: list
        """
        if raw:
            return super(Kraken, self)._get_trades(pair, file)
        else:
            js = super(Kraken, self)._get_trades(pair, file)
            for key in js['result']:
                if key is not 'last':
                    return js['result'][key]

    def ticker(self, pair, raw=False, file=None):
        """
        Returns a dictionary with ticker data. If raw is True, we'll return the
        raw json query.
        :param pair: str
        :param raw: bool
        :return: dict
        """
        if raw:
            return super(Kraken, self)._get_ticker(pair, file)
        else:
            js = super(Kraken, self)._get_ticker(pair, file)
            for key in js['result']:
                return js['result'][key]

    def buy_budget(self, budget, pair):
        """
        Return the maximum amount of currency purchasable with the given budget.
        :param budget: float/int
        :param pair: str
        :return: float
        """
        a, _ = self.ob(pair)
        return super(Kraken, self)._trade_budget(budget, a)

    def buy_vol(self, vol, pair):
        """
        Return the total price for the given volume.
        :param vol: float/int
        :param pair: str
        :return: float
        """
        a, _ = self.ob(pair)
        return super(Kraken, self)._trade_vol(vol, a)

    def sell_vol(self, vol, pair):
        """
        Return total expected return for given volume of currency
        :param vol:
        :param pair:
        :return:
        """
        _, b = self.ob(pair)
        return super(Kraken, self)._trade_vol(vol, b)

    def sell_profit(self, profit, pair):
        """
        Return total volume required to obtain the given profit margin.
        :profit: float/int
        :pair: str
        :return: float
        """
        _, b = self.ob(pair)
        return super(Kraken, self)._trade_budget(profit, b)