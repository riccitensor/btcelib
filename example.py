from btcelib.Kraken import Kraken

kraken = Kraken()

for pair in kraken.pairs:
    print(kraken.ticker(pair))

print(kraken)