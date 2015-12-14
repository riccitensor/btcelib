"""
apiHandler.py functions cover anything regarding creating, accessing and
managing .api files;
"""

import json
import logging
import os

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
    for i, pair in enumerate(pairs):
        api[name][pair] = {}
        for ii, url in enumerate(urls[i]):
            api[name][pair][key[ii]] = url

    with open(file, 'w+') as f:
        json.dump(api, f)

    return file


def load_api(file):
    """
    Loads a given .api file.
    :param file: name of the file (inclusive path if anywhere else saved than script's path)
    :return: dictionary of api attributes
    """
    with open(file, 'r') as f:
        js = json.load(f)
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
            print(file)
            api = load_api('%s%s' % (src,file))
            for key in api:
                apis[key] = api[key]

    return apis


if __name__ == '__main__':
    name = 'test'
    pairs = ['a_b', 'c_d']
    urls = [['1','2','3'],['4','5','6']]

    save_api(name, pairs, urls)
    d = load_api('test.api')
    print(d['test'])
