import logging

logging.basicConfig(level=logging.DEBUG,
                    datefmt='%m-%d %H:%M',
                    filename='kraken_returns.log',
                    filemode='w+')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s %(name)-4s: %(levelname)-4s %(message)s')
console.setFormatter(formatter)

log = logging.getLogger()


import btcelib as btc

kraken = btc.exchanges.Kraken()

#print(kraken.ticker('XBTLTC'))
#print(kraken.trades('XBTLTC'))
#print(kraken.ob('XBTLTC'))

print(kraken.buy_budget(100, 'XBTEUR'))
print(kraken.buy_vol(100, 'LTCEUR'))
