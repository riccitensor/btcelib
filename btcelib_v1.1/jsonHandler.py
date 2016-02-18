"""
Handles fetching json data from url, and packing/unpacking it to files.
"""

import urllib.request
import logging
import json

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
    :return: File
    """
    if data is None:
        log.error("Input is 'None' - no json detected!")
        raise ValueError

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
    """
    Loads json data from a given file and writes debugging data to log files.
    :param file: file name containing json
    :return:
    """
    with open(file, 'r') as f:
        try:
            js = json.load(f)
            log.debug(file)
            log.info("JSON data loaded successfully!")
            return js
        except Exception as e:
            log.error("Error while loading json data! %s", e)
            return


def pack_tar(prefix, arch_name, fp='./', cleanup=False):
    """
    Packs all files that start with the string given as prefix and packs them
    into a tarball.
    :param prefix: string files start with
    :param arch_name: name of the resulting tarball
    :param fp: filepath to look for the files in
    :param cleanup: remove compressed files; default off
    :return: bool
    """
    files = []
    for file in os.listdir(fp):
        if file.startswith(prefix):
            files.append(file)

    with tar.open(arch_name, "w:gz") as f:
        for file in files:
            try:
                f.add("%s%s" % (fp,file), recursive=False)
            except FileNotFoundError as e:
                log.error("File not found! Not adding it to tarball! %s", e)
                continue
            except Exception as e:
                log.error("Unexpected Error raised during packing! %s", e)
                raise

    for file in files:
        try:
            os.remove("%s%s" % (fp,file))
        except FileNotFoundError:
            log.warning("File %s not found! Skipping deletion!", file)
            continue
        except Exception as e:
            log.error("Unexpected Error raised during cleanup! %s", e)
            raise

    return True


def unpack_tar(fname, fp='./'):
    """
    unpacks a tar file which has been packaged with pack_tar().
    :param fname: file name
    :param fp: folder of tar
    :return: bool
    """
    full_path = '%s%s' % (fp, fname)

    if tar.is_tarfile(full_path):
        with tar.open(full_path, 'r:gz') as archive:
            archive.extractall()
            return True
    else:
        return False

if __name__ == '__main__':
    print(0)
