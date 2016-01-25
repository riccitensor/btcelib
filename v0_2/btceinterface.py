
import apiHandler
import jsonHandler
import logging
import btceutility

log = logging.getLogger(__name__)


class Api:
    """
    Creates an Api object used to interact with the api stored in file.
    """
    def _log(self):
        """
        Private function; Debugging; Prints all attributes of this class to
        console; it's also automatically logged to a logfile; this can be turned
        off by passing log=False.
        :return: None
        """
        log.info("Logging api() class variables to console..")
        attrs = self._attrs()
        if attrs:
            for attr in attrs:
                log.debug("self.{0} = {1}".format(attr, attrs[attr]))
        else:
            log.debug("self.{0} = {1}".format(attrs, attrs))
        log.info("api()._log() complete.")
        return

    def __init__(self, file):
        self.name = ''
        self.pairs = {}
        self.data = {}
        self.ticker = {}
        self.trades = {}
        self.ob = {}


        inp = apiHandler.load_api(file)
        self.data = inp
        for key in inp:
            self.name = key
            for pair in inp[key]:
                self.pairs[pair] = pair
        self._log()

    def _attrs(self):
        """
        Returns a list of class' attributes.
        :return:
        """
        attrs = {'name': self.name, 'pairs': self.pairs, 'data': self.data}
        return attrs

    def check_pair(self, pair=None):
        """
        Interface function, used to check if a pair exists in this class. By
        default, this function checks if there is at least 1 pair present, and
        writes the self.pair var to the logs.
        :param pair: string containing pair name
        :return: bool
        """
        if pair is None:
            log.debug("No pair specified; checking if self.pairs is empty..")
            if len(self.pairs) > 0:
                log.info("dict not empty; %s items found!", len(self.pairs))
                log.debug(self.pairs)
                return True
            else:
                log.error("self.pairs is an empty dict!")
                return False
        else:
            if pair in self.pairs:
                log.debug("Pair %s exists in self.pairs!", pair)
                return True
            else:
                log.debug("Pair %s does not exist in self.pairs!", pair)
                return False

    def _get(self, pair, d_type, save, file):
        """
        Subroutine, which fetches json from url using jsonHandler.fetch_json()
        :param pair: currency pair to use from class' data attribute
        :param d_type: data type to grab - is either 'ticker', 'orderbook' or
        'transactionHistory'.
        :param save: bool, save to file yes/no
        :param file: path with filename for saving
        :return: returns json if successful, otherwise returns None.
        """

        try:
            url = self.data[self.name][pair][d_type]
            d = jsonHandler.fetch_json(url)

        except KeyError:
            log.error("No such key! Entry doesn't exist! KeyError!")
            log.debug("Used Keys were [%s][%s][%s]", (self.name, pair, d_type))
            return None

        if save:
            jsonHandler.pack_json(d, file)
            log.debug("Data written to file at {0}!".format(file))
        return d

    def get_orderbook(self, pair, save=False, file='./orderbook.json', update=True):
        """
        Interface function to get orderbook as dictionary
        :param pair: currency pair to get.
        :param save: bool, save to file yes/no
        :param file: path with filename for saving
        :param update: Store data in class bool
        :return: dictionary with json data or None (if unsuccessful)
        """
        if self.check_pair(pair):
            if update:
                self.ob = self._get(pair, 'orderbook', save, file)
                return self.ob
            else:
                return self._get(pair, 'orderbook', save, file)
        else:
            log.error("Pair not found! String may be invalid or self.pair "
                      "attribute empty! Returning 'None'..")
            return None

    def get_transactions(self, pair, save=False, file='./transactions.json', update=True):
        """
        Interface function to get transactionHistory as dictionary
        :param pair: currency pair to get.
        :param save: bool, save to file yes/no
        :param file: path with filename for saving
        :param update: Store data in class bool
        :return: dictionary with json data or None (if unsuccessful)
        """
        if self.check_pair(pair):
            if update:
                self.trades = self._get(pair, 'transactionHistory', save, file)
                return self.trades
            else:
                return self._get(pair, 'transactionHistory', save, file)
        else:
            log.error("Pair not found! String may be invalid or self.pair "
                      "attribute empty! Returning 'None'..")
            return None

    def get_ticker(self, pair, save=False, file='./tickers.json', update=True):
        """
        Interface function to get ticker as dictionary
        :param pair: currency pair to get.
        :param save: bool, save to file yes/no
        :param file: path with filename for saving
        :param update: Store data in class bool
        :return: dictionary with json data or None (if unsuccessful)
        """
        if self.check_pair(pair):
            if update:
                self.ticker = self._get(pair, 'ticker', save, file)
                return self.ticker
            else:
                return self._get(pair, 'ticker', save, file)
        else:
            log.error("Pair not found! String may be invalid or self.pair "
                      "attribute empty! Returning 'None'..")
            return None

    def plot_ob(self):
        #do stuff

    def plot_transactions(self):
        #do stuff

    def plot_ticker(self):








