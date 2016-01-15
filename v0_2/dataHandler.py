import logger


log = logging.getLogger(__name__)

def convert_th(th):
    #do stuff

def convert_ticker(tickers):
    opens = []
    closes = []
    highs = []
    lows = []
    volumes = []
    timestamps = []
    for ticker in tickers:
        opens.append(ticker['open'])
        closes.append(ticker['close'])
        highs.append(ticker['high'])
        lows.append(ticker['low'])
        volumes.append(ticker['volume'])
        timestamps.append(ticker['timestamp'])
    return {'open': opens, 'close': closes, 'high': highs, 'low': lows,
            'volume': volumes, 'timestamp': timestamps}


def convert_ob(ob):
    bids = ob['bids']
    asks = ob['asks']

    bids_value = []
    bids_amount = []
    asks_value = []
    asks_amount = []

    log.info('Separating bids..')
    for bid in bids:
        try:
            log.debug('Splitting %s ..', bid)
            bids_value.append(bid[0])
            bids_amount.append(bid[1])
            log.debug('successful!')
        except IndexError as e:
            log.error('IndexError while splitting %s! Skipping..', bid)
            log.debug(e)
            continue
    for ask in asks:
        try:
            log.debug('Splitting %s ..', ask)
            asks_value.append(ask[0])
            asks_amount.append(ask[1])
            log.debug('successful!')
        except IndexError as e:
            log.error('IndexError while splitting %s! Skipping..', ask)
            log.debug(e)
            continue

    return [bids_amount, bids_value, asks_amount, asks_value]

