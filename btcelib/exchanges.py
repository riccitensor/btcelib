from btcelib.exchanges import Exchange

'''
Define Built-in Exchanges
'''


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
