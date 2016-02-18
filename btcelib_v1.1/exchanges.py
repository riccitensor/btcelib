import logging
import jsonHandler
import decimal

log = logging.getLogger(__name__)


class Exchange():
    """
    Comes with base functions for class extensions; i.e. _get_orderbook() to get
    the base json from the api as specified on initialization;

    """

    def __init__(self, url, query_mask, pairs, types, name):
        """
        initializes base-class.

        :param url: str, url to api
        :param query_mask: str
        :param pairs: {'pair1': str, 'pair2': str, ... }
        :param types: {'ticker': str, 'trades': str, 'orderbook':str}
        :param name: str, name of exchange; usually homepage
        :return:
        """
        self.name = name
        self.url = url
        self.mask = query_mask
        self.pairs = pairs
        self.types = types

    def load(self, url=None, query_mask=None, pairs=None, types=None, name=None):
        c = 0
        if url is not None:
            self.url = url
        if query_mask is not None:
            self.mask = query_mask
        if pairs is not None:
            self.pairs = pairs
        if types is not None:
            self.types = types
        if name is not None:
            self.name = name
        return

    def _is_pair(self, pair):
        if pair in self.pairs:
            return True
        else:
            return False

    def make_query(self, t, p):
        try:
            m = self.mask.format(_type=t, pair=p)
        except KeyError:
            m = self.mask.format(pair=p, _type=t)

        return self.url + m

    def _get_orderbook(self, pair):
        if self._is_pair(pair):
            return jsonHandler.fetch_json(self.make_query(self.types['orderbook'],
                                                    self.pairs[pair]))
        else:
            raise ValueError('{} is not a tradeable pair at{}'.format(pair, self.name))

    def _get_ticker(self, pair):
        if self._is_pair(pair):
            return jsonHandler.fetch_json(self.make_query(self.types['ticker'],
                                                      self.pairs[pair]))
        else:
            raise ValueError('{} is not a tradeable pair at{}'.format(pair, self.name))

    def _get_trades(self, pair):
        if self._is_pair(pair):
            return jsonHandler.fetch_json(self.make_query(self.types['trades'],
                                             self.pairs[pair]))
        else:
            raise ValueError('{} is not a tradeable pair at{}'.format(pair, self.name))

    def _trade_price(self, pair, amount, offers):
        """
        Calculates total price for given amount and offers. Can be used to calc
        sell or buy price.
        :param pair: str
        :param amount: float or int
        :param bids: list of lists format[price, vol, timestamp]
        :return:
        """
        basket = 0.0
        left_to_trade = amount
        total = 0.0
        for offer in offers:
            p = offer[0]
            vol = offer[1]
            if left_to_trade > 0.0:
                if vol > left_to_trade:
                    basket += left_to_trade
                    left_to_trade -= left_to_trade
                    total += left_to_trade * p
                elif vol < amount:
                    basket += vol
                    left_to_trade -= vol
                    total += vol * p
        return total

    def _trade_vol(self, sum_, offers):
        """
        Calculates maximum volume purchasabale with given money sum and offers.
        Usable for both sell and buy offers.
        :param amount: int or float
        :param offers: list of lists in format [price, vol, timestamp]
        :return: float
        """
        wallet = sum_
        basket = decimal.Decimal(0.0)

        for offer in offers:
            p = offer[0]
            vol = offer[1]
            if wallet > 0.0:
                if p * vol <= wallet:
                    wallet -= p * vol
                    basket += vol
                elif p * vol > wallet:
                    wallet -= wallet
                    basket += decimal.Decimal(wallet / p).quantize(Decimal('0.00000001'), rounding=ROUND_DOWN)
        return float(basket)


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
