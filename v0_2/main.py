import jsonHandler

apis = [{'Coinbase':{
'EUR':{
'ticker': 'https://api.exchange.coinbase.com/products/BTC-EUR/ticker',
'orderbook': 'https://api.exchange.coinbase.com/products/BTC-EUR/book?level=3',
'transactionHistory': 'https://api.exchange.coinbase.com/products/BTC-EUR/trades'},
'USD':{
'ticker': 'https://api.exchange.coinbase.com/products/BTC-USD/ticker',
'orderbook': 'https://api.exchange.coinbase.com/products/BTC-USD/book?level=3',
'transactionHistory': 'https://api.exchange.coinbase.com/products/BTC-USD/trades'}
}},
{'itBit':{
'EUR':{
'ticker': 'https://api.itbit.com/v1/markets/XBTEUR/ticker',
'orderbook': 'https://api.itbit.com/v1/markets/XBTEUR/order_book',
'transactionHistory': 'https://api.itbit.com/v1/markets/XBTEUR/trades'},
'USD':{
'ticker': 'https://api.itbit.com/v1/markets/XBTUSD/ticker',
'orderbook': 'https://api.itbit.com/v1/markets/XBTUSD/order_book',
'transactionHistory': 'https://api.itbit.com/v1/markets/XBTUSD/trades'}
}},
{'RockTradingCompany':{
'EUR':{
'ticker': 'api.therocktrading.com/v1/funds/BTCEUR/ticker',
'orderbook': 'api.therocktrading.com/v1/funds/BTCEUR/orderbook',
'transactionHistory': 'api.therocktrading.com/v1/funds/BTCEUR/trades'},
'USD':{
'ticker': 'api.therocktrading.com/v1/funds/BTCUSD/ticker',
'orderbook': 'api.therocktrading.com/v1/funds/BTCUSD/orderbook',
'transactionHistory': 'api.therocktrading.com/v1/funds/BTCUSD/trades'}
}},
{'Hitbtc':{
'USD':{
'ticker': 'http://api.hitbtc.com/api/1/public/BTCUSD/ticker',
'orderbook': 'http://api.hitbtc.com/api/1/public/BTCUSD/orderbook',
'transactionHistory': 'http://api.hitbtc.com/api/1/public/BTCUSD/trades'},
'EUR':{
'ticker': 'http://api.hitbtc.com/api/1/public/BTCEUR/ticker',
'orderbook': 'http://api.hitbtc.com/api/1/public/BTCEUR/orderbook',
'transactionHistory': 'http://api.hitbtc.com/api/1/public/BTCEUR/trades'}
}},
{'Btc-e':{
'USD':{
'ticker': 'https://btc-e.com/api/3/ticker/btc_usd',
'orderbook': 'https://btc-e.com/api/3/depth/btc_usd',
'transactionHistory': 'https://btc-e.com/api/3/trades/btc_usd'}
}},
{'Bitbay':{
'EUR':{
'ticker': 'https://bitbay.net/API/Public/BTCEUR/ticker.json',
'orderbook': 'https://bitbay.net/API/Public/BTCEUR/orderbook.json',
'transactionHistory': 'https://bitbay.net/API/Public/BTCEUR/trades.json'},
'USD': {
'ticker': 'https://bitbay.net/API/Public/BTCUSD/ticker.json',
'orderbook': 'https://bitbay.net/API/Public/BTCUSD/orderbook.json',
'transactionHistory': 'https://bitbay.net/API/Public/BTCUSD/trades'}
}}
]

for i, api in enumerate(apis):
    for exchange in apis[i]:
        jsonHandler.pack_json(apis[i], '/home/nls/git/btcelib/API/{0}.api' %s (exchange))