import logging
import jsonHandler

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

'''
Define Built-in Exchanges
'''

class Kraken(Exchange):
    def __init__(self):
        name='Kraken.com'
        query_mask='{_type}?pair={pair}'
        url='https://api.kraken.com/0/public/'
        pairs={}
        types={'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Bitbay(Exchange):
    def __init__(self):
        name='bitbay.net'
        query_mask='{pair}/{_type}.json'
        url='https://bitbay.net/API/Public/'
        pairs={}
        types={'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Bitstamp(Exchange):
    def __init__(self):
        name='bitstamp.net'
        query_mask='{_type}/{pair}'
        url='https://www.bitstamp.net/api/'
        pairs={}
        types={'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Btce(Exchange):
    def __init__(self):
        name='btc-e.com'
        query_mask='{_type}/{pair}'
        url='https://btc-e.com/api/3/'
        pairs={}
        types={'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Cex(Exchange):
    def __init__(self):
        name='cex.io'
        query_mask='{_type}/{pair}'
        url='https://cex.io/api/'
        pairs={}
        types={'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Coinbase(Exchange):
    def __init__(self):
        name='coinbase.com'
        query_mask='{pair}/{_type}'
        url='https://api.exchange.coinbase.com/products/'
        pairs={}
        types={'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Hitbtc(Exchange):
    def __init__(self):
        name='hitbtc.com'
        query_mask='{pair}/{_type}'
        url='http://api.hitbtc.com/api/1/public/'
        pairs={}
        types={'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class itBit(Exchange):
    def __init__(self):
        name='itbit.com'
        query_mask='{pair}/{_type}'
        url='https://api.itbit.com/v1/markets/'
        pairs={}
        types={'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class TheRockTradingCompany(Exchange):
    def __init__(self):
        name='therocktrading.com'
        query_mask='{pair}/{_type}'
        url='https://api.therocktrading.com/v1/funds/'
        pairs={}
        types={'orderbook': '', 'ticker':'', 'trades': ''}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)
