"""
Handles fetching json data from url, and packing/unpacking it to files.
"""

import urllib.request
import logging
import json
import gzip
import shutil

log = logging.getLogger(__name__)



def fetch_json(url):
    """
    Retrieves json data from given url, using urllib.request
    :param url: url to parse
    :return: dictionary
    """
    js = {}

    try:
        response = urllib.request.urlopen(url)
        log.debug(url)
        log.info("URL opened successfully!")

    except Exception as e:
        log.error("Error while requesting data from URL! %s", e)
        return None

    try:
        js = json.loads(response.read().decode('utf-8'))
        log.debug(js)
        log.info("Loading JSON successful.")
        return js
    except Exception as e:
        log.error("Error while loading json data from url! %s", e)
        return None


def pack_json(data, file):
    """
    Uses json.dump to pack a dictionary into a file with the .json extension.
    :param data: dictionary
    :param file: file, incl path if different from path of executing script
    :param compress: t/f flag for the compression option
    :return: true / false
    """
    if data is None:
        log.error("Input is 'None' - no json detected! Skipping file packing!")
        return None

    with open(file, 'w+') as f:
        try:
            json.dump(data, f)
            log.debug(data)
            log.info("Dumping JSON to file successful!")

        except Exception as e:
            log.debug(data)
            log.debug(f)
            log.error("Error while dumping json data to file! %s", e)

    return file


def unpack_json(file):

    with open(file) as f:
        try:
            js = json.load(f)
            log.debug(file)
            log.info("JSON data loaded successfully!")
            return js
        except Exception as e:
            log.error("Error while loading json data!", e)
            return

def unpackarchive(archivefile):
    print()

if __name__ == '__main__':
    print(1)

