import logging
import jsonHandler

log = logging.getLogger(__name__)

class Exchange():
    def __init__(self, url, query_mask, pairs, types, name):
        self.name = name
        self.url = url
        self.mask = query_mask
        self.pairs = pairs
        self.types = types
    def make_query(self, _type, pair):
        try:
            m = self.mask.format(_type=t, pair=p)
        except KeyError:
            m = self.mask.format(pair=p, _type=t)

        return self.url + m

    def get_orderbook(self, pair):

        make_query(self.types['orderbook'], self.pairs[pair])

class Kraken(Exchange):
    def __init__(self):
        name='Kraken.com'
        query_mask='{_type}?pair={pair}'
        url='https://api.kraken.com/0/public/'
        pairs={}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Bitbay(Exchange):
    def __init__(self):
        name='Kraken.com'
        query_mask='{pair}/{_type}.json'
        url='https://bitbay.net/API/Public/'
        pairs={}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Bitstamp(Exchange):
    def __init__(self):
        name='Kraken.com'
        query_mask='{_type}/{pair}'
        url='https://www.bitstamp.net/api/'
        pairs={}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Btce(Exchange):
    def __init__(self):
        name='Kraken.com'
        query_mask='{_type}/{pair}'
        url='https://btc-e.com/api/3/'
        pairs={}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Cex(Exchange):
    def __init__(self):
        name='Kraken.com'
        query_mask='{_type}/{pair}'
        url='https://cex.io/api/'
        pairs={}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Coinbase(Exchange):
    def __init__(self):
        name='Kraken.com'
        query_mask='{pair}/{_type}'
        url='https://api.exchange.coinbase.com/products/'
        pairs={}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class Hitbtc(Exchange):
    def __init__(self):
        name='Kraken.com'
        query_mask='{pair}/{_type}'
        url='http://api.hitbtc.com/api/1/public/'
        pairs={}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class itBit(Exchange):
    def __init__(self):
        name='Kraken.com'
        query_mask='{pair}/{_type}'
        url='https://api.itbit.com/v1/markets/'
        pairs={}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)

class TheRockTradingCompany(Exchange):
    def __init__(self):
        name='Kraken.com'
        query_mask='{pair}/{_type}'
        url='https://api.therocktrading.com/v1/funds/'
        pairs={}
        super(Kraken, self).__init__(url, query_mask, pairs, types, name)


if __name__ == '__main__':
    mask = '{a} then {b}'
    a = 'Blergh'
    b = 'Ugh'
    try:
        print(mask.format(b=b, a=a))
    except KeyError:
        print('Whoops.')
        print(mask.format(a=a,b=b))