import logging
from btcelib.Kraken import Kraken

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


kraken = Kraken()

for pair in kraken.pairs:
    print(kraken.ticker(pair))

print(kraken)