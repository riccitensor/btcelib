import logging
import btcelib.jsonHandler as jsonHandler

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

    def _trade_vol(self, amount, offers):
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
            p = float(offer[0])
            vol = float(offer[1])
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

    def _trade_budget(self, sum_, offers):
        """
        Calculates maximum volume purchasabale with given money sum and offers.
        Usable for both sell and buy offers.
        :param amount: int or float
        :param offers: list of lists in format [price, vol, timestamp]
        :return: float
        """
        wallet = sum_
        basket = 0.0

        for offer in offers:
            p = float(offer[0])
            vol = float(offer[1])
            if wallet > 0.0:
                if p * vol <= wallet:
                    wallet -= p * vol
                    basket += vol
                elif p * vol > wallet:
                    wallet -= wallet
                    basket += (wallet / p)
        return basket


