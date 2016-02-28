import logging
import btcelib.jsonHandler as jsonHandler
import decimal


log = logging.getLogger(__name__)


class Exchange:
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

    def __str__(self):
        s = "Name: {}\nBase Url: {}\nQuery Mask: {}\nAvailable Pairs: {}\n" \
            "Types: {}".format(self.name, self.url, self.mask, self.pairs, self.types)
        return s

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

    def _get_data(self, pair, _type, file):
        if self._is_pair(pair)_:
            if file is not None:
                jsonHandler.unpack_json(file)
            return jsonHandler.fetch_json(self.make_query(self.types[_type],
                                                          self.pairs[pair]))
        else:
            raise ValueError('{} is not a tradeable pair at{}'.format(pair,
                                                                      self.name))

    def _get_orderbook(self, pair, file=None):
        return self._get_data(pair, 'orderbook', file)

    def _get_ticker(self, pair, file=None):
        return self._get_data(pair, 'ticker', file)

    def _get_trades(self, pair, file=None):
        return self._get_data(pair, 'trades', file)

    def _trade_vol(self, amount, offers):
        """
        Calculates total price for given amount and offers. Can be used to calc
        sell or buy price.
        :param pair: str
        :param amount: float or int
        :param bids: list of lists format[price, vol, timestamp]
        :return:
        """
        d = decimal.Decimal
        decimal.getcontext().prec = 8
        decimal.getcontext().rounding = decimal.ROUND_DOWN
        basket = d(0.0)
        left_to_trade = d(amount)
        total = d(0.0)
        for offer in offers:
            p = d(offer[0])
            vol = d(offer[1])
            if left_to_trade > d(0.0):
                if vol > left_to_trade:
                    total += left_to_trade * p
                    left_to_trade -= left_to_trade
                elif vol < amount:
                    left_to_trade -= vol
                    total += vol * p
        return float(total)

    def _trade_budget(self, sum_, offers):
        """
        Calculates maximum volume purchasabale with given money sum and offers.
        Usable for both sell and buy offers.
        :param amount: int or float
        :param offers: list of lists in format [price, vol, timestamp]
        :return: float
        """
        d = decimal.Decimal
        decimal.getcontext().prec = 8
        decimal.getcontext().rounding = decimal.ROUND_DOWN
        wallet = d(sum_)
        basket = d(0.0)
        for offer in offers:
            p = d(offer[0]) # convert string to float
            vol = d(offer[1]) # convert string to float
            if wallet > 0.0:
                if p * vol <= wallet:
                    wallet -= p * vol
                    basket += vol
                elif p * vol > wallet:
                    basket += wallet / p
                    wallet -= wallet

        return float(basket)


