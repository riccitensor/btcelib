import apiHandler
import jsonHandler

def get(api, pair, json):

    if hasattr(api, 'read'):
        exchange = api.split('.')[0]
        d = apiHandler.loadApi(api)
        d[exchange][pair][json]
    else:
        url = api[pair][json]

    data = jsonHandler.fetchjson(url)
    return data

def orderbook(api, pair):
    return get(api, pair, 'orderbook')


def transactions(api):
    return get(api, pair, 'transactionHistory')


def ticker(api):
    return get(api, pair, 'ticker')

