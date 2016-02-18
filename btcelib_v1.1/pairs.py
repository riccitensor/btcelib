import logging
import jsonHandler

logging.basicConfig(level=logging.DEBUG,
                    datefmt='%m-%d %H:%M',
                    filename='btce_bot.log',
                    filemode='w+')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s %(name)-4s: %(levelname)-4s %(message)s')
console.setFormatter(formatter)

log = logging.getLogger()

class Pair():
    def __init__(self, pair):
        self.pair = pair
        self.url = {'ticker':'https://api.kraken.com/0/public/Ticker?pair=',
                   'ob':'https://api.kraken.com/0/public/Depth?pair=',
                   'trades':'https://api.kraken.com/0/public/Trades?pair='}

    def get_ob(self):
        js = jsonHandler.fetch_json(self.url['ob'] + self.pair)
        ob = {}
        for key in js['result']:
            ob = js['result'][key]
        a = ob['asks'].sort() #lowest selling price first
        b = ob['bids'].sort(reverse=True) #highest buying price first
        return a, b

    def get_trades(self):
        js = jsonHandler.fetch_json(self.url['trades'] + self.pair)
        trades = {}
        for key in js['result']:
            trades = js['result'][key]
        return trades

    def get_ticker(self):
        js = jsonHandler.fetch_json(self.url['ticker'] + self.pair)
        ticker = {}
        for key in js['result']:
            ticker = js['result'][key]
        return ticker

    def best_price(self):
        a, b = self.get_ob()
        return a[0], b[0]

    def batch_price(self, amount, order='buy'):
        """
        Return avg price per unit if buying given amount
        :param amount:
        :param order:
        :return:
        """

        book = []
        total = 0.0
        basket = 0.0
        if order is 'buy':
            book, _ = self.get_ob()
        elif order is 'sell':
            _, book = self.get_ob()
        else:
            raise ValueError('Key argument \'order\' can only be \'sell\' or \'buy\'.')

        for offer in book:
            #offer[0] is price, offer[1] is vol
            if amount - basket >= offer[1]:
                #add all of order to basket
                total +=  offer[0] * offer[1]
                basket += offer[1]
            elif amount - basket < offer[1]:
                #add amount-basket to basket
                total += offer[0] * (amount - basket)
                basket += amount - basket
        return total / amount
