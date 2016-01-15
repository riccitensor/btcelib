"""
apiHandler.py functions cover anything regarding creating, accessing and
managing .api files;
"""

import json
import logging
import os
import btceutility

log = logging.getLogger(__name__)


def save_api(name, pairs, urls, target='./'):
    """
    Converts the given string and lists into a json file at given path.

    :param name: name of the exchange
    :param pairs: list of pairs to be added for this exchange; i.e. [pair, ..];
    must be a list!
    :param urls: list of lists of url; i.e. [[url1,url2,urls3]]
    must be a list!
    :param target: desired destination for the created file.
    :return: returns the name of the created file
    """
    file = '%s%s.api' % (target, name)
    key = ['ticker', 'orderbook', 'transactionHistory']
    api = {name: {}}
    try:
        for i, pair in enumerate(pairs):
            api[name][pair] = {}
            log.info("Entry for pair %s created successfully!", pair)
            log.debug("%s[%s][%s]", (api, name, pair))
            for ii, url in enumerate(urls[i]):
                api[name][pair][key[ii]] = url
                log.info("Url written to key successfully")
                log.debug("%s[%s][%s][%s[%s]] = %s", (api, name, pair, key, ii))
    except KeyError as e:
        log.error("A Key wasn't not found!")
        log.debug(e)

    except IndexError as e:
        log.error("An Index wasn't found!")
        log.debug(e)

    with open(file, 'w+') as f:
        try:
            json.dump(api, f)
            log.info("Json data written to file successfully!")
            log.debug(api)
            log.debug(f)
        except Exception as e:
            log.error("Exception during JSON dump to file! %s", e)
            raise
    return file


def add_api():
    """
    Interactive way to create  a bitcoin Api as a .api file;
    :return: file name of created .api file
    """
    print("Starting interactive API Addition sequence..\n")
    print("Enter name of api:\n")
    name = ''
    name = btceutility.get_conf('name', name)
    print("Enter pairs ( separate multiple entries by ','):")
    pairs_input = ''
    pairs_input = btceutility.get_conf('pairs', pairs_input)
    pairs_input = pairs_input.strip(' ')
    print(pairs_input)
    pairs = pairs_input.split(',')
    print(pairs)
    print("Now starting loop for urls..\n")
    print("please enter urls for each pair..")
    urls = []
    for item in pairs:
        print("Enter Ticker url:")
        ticker = ''
        ticker = btceutility.get_conf('%s:ticker' % item, ticker)
        print("Enter orderBook url:")
        orderbook = ''
        orderbook = btceutility.get_conf('%s:orderbook' % item, orderbook)
        print("Enter TransactionHistory url:")
        th = ''
        th = btceutility.get_conf('%s:transactionhistory' % item, th)
        urls.append([ticker, orderbook, th])
    print("Where would you like to save your .api file?")
    target = ''
    target = btceutility.get_conf('targetdir', target)
    print("Interactive sequence complete.")
    print("Creating .api file..")
    fname = save_api(name, pairs, urls, target)
    print("Complete.\n")
    log.info("add_api() Complete.")
    return fname


def load_api(file):
    """
    Loads a given .api file.
    :param file: name of the file (inclusive path if anywhere else saved than script's path)
    :return: dictionary of api attributes
    """
    with open(file, 'r') as f:
        js = json.load(f)
        log.info("Loading of .api file successful!")
        log.debug(f)
    return js


def init_api(src='./'):
    """
    Loads all .api files in given directory
    :param src: directory to check - does not walk up or down.
    :return: dictionary of all loaded apis
    """
    files = os.listdir(src)
    apis = {}
    for file in files:
        if file.endswith('.api'):
            log.info("File found! loading api..")
            log.debug(file)
            api = load_api('%s%s' % (src, file))
            for key in api:
                apis[key] = api[key]

    return apis


if __name__ == '__main__':
    name = 'test'
    pairs = ['a_b', 'c_d']
    urls = [['1', '2', '3'], ['4', '5', '6']]

    save_api(name, pairs, urls)
    add_api()
    d = load_api('test.api')
    print(d['test'])
