from btcelib.exchange import Exchange

'''
Define Built-in Exchanges
'''


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

    def ob(self, pair, raw=False):
        """
        Returns two lists, asks & bids. If raw is True, we'll return the raw
        json query.
        :param pair: str
        :param raw: bool
        :return: list, list
        """
        if raw:
            return super(Kraken, self)._get_orderbook(pair)
        else:
            js = super(Kraken, self)._get_orderbook(pair)
            for key in js['result']:
                a = js['result'][key]['asks']
                b = js['result'][key]['bids']
                return a, b

    def trades(self, pair, raw=False):
        """
        Returns list of trades from JSON query. If raw is True, we'll return the
        raw json query.
        :param pair: str
        :param raw: bool
        :return: list
        """
        if raw:
            return super(Kraken, self)._get_trades(pair)
        else:
            js = super(Kraken, self)._get_trades(pair)
            for key in js['result']:
                if key is not 'last':
                    return js['result'][key]

    def ticker(self, pair, raw=False):
        """
        Returns a dictionary with ticker data. If raw is True, we'll return the
        raw json query.
        :param pair: str
        :param raw: bool
        :return: dict
        """
        if raw:
            return super(Kraken, self)._get_ticker(pair)
        else:
            js = super(Kraken, self)._get_ticker(pair)
            for key in js['result']:
                return js['result'][key]

    def buy_budget(self, budget, pair):
        a, _ = self.ob(pair)
        return super(Kraken, self)._trade_budget(budget, a)

    def buy_vol(self, vol, pair):
        a, _ = self.ob(pair)
        return super(Kraken, self)._trade_vol(vol, a)


class Bitbay(Exchange):
    def __init__(self):
        name = 'bitbay.net'
        query_mask = '{pair}/{_type}.json'
        url = 'https://bitbay.net/API/Public/'
        pairs = {}
        types = {'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)


class Bitstamp(Exchange):
    def __init__(self):
        name = 'bitstamp.net'
        query_mask = '{_type}/{pair}'
        url = 'https://www.bitstamp.net/api/'
        pairs = {}
        types = {'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)


class Btce(Exchange):
    def __init__(self):
        name = 'btc-e.com'
        query_mask = '{_type}/{pair}'
        url = 'https://btc-e.com/api/3/'
        pairs = {}
        types = {'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)


class Cex(Exchange):
    def __init__(self):
        name = 'cex.io'
        query_mask = '{_type}/{pair}'
        url = 'https://cex.io/api/'
        pairs = {}
        types = {'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)


class Coinbase(Exchange):
    def __init__(self):
        name = 'coinbase.com'
        query_mask = '{pair}/{_type}'
        url = 'https://api.exchange.coinbase.com/products/'
        pairs = {}
        types = {'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)


class Hitbtc(Exchange):
    def __init__(self):
        name = 'hitbtc.com'
        query_mask = '{pair}/{_type}'
        url = 'http://api.hitbtc.com/api/1/public/'
        pairs = {}
        types = {'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)


class itBit(Exchange):
    def __init__(self):
        name = 'itbit.com'
        query_mask = '{pair}/{_type}'
        url = 'https://api.itbit.com/v1/markets/'
        pairs = {}
        types = {'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)


class TheRockTradingCompany(Exchange):
    def __init__(self):
        name = 'therocktrading.com'
        query_mask = '{pair}/{_type}'
        url = 'https://api.therocktrading.com/v1/funds/'
        pairs = {}
        types = {'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)
