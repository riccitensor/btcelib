import logging
import math

log = logging.getLogger(__name__)

def get_conf(varname, var):
    """
    Loop for interactive prompts. returns true once finished.
    :param varname: String, containing name of the variable
    :param var: variable itself.
    :return: True, once done.
    """
    conf = False
    while conf is False:
        print("Please enter a value for %s:" % varname)
        var = input()
        print("Is the spelling correct? %s" % var)
        fb = input("[yes.]")
        if fb == '' or fb == 'y' or fb == 'yes':
            print("Input accepted. Moving on..")
            log.debug("User input for api %s : %", (varname, var))
            conf = True
        elif fb == 'n' or fb == 'no':
            continue
        else:
            print("Please type 'yes' or 'no'.\n")
    return var


def is_dict(obj):
    """
    Checks if the object is a dictionary
    :param obj:
    :return: T/F
    """
    if isinstance(obj, dict):
        return True
    else:
        return False


def _decode(d):
    """
    encodes given dictionary keys to ascii.
    :param d: dict
    :return: dict
    """
    return dict((k.encode(), v) for (k, v) in d.items())


def _decode_list(l):
    """
    iterates through given list and calls decode function according to type
    :param l:
    :return:
    """
    new_l = []
    for item in l:
        if isinstance(item, dict):
            dec = _decode(item)
            new_l.append(recursive_decode(dec))
        elif isinstance(item, list):
            new_l.append(_decode_list(item))
    return new_l


def recursive_decode(d):
    """
    traverses all elements of a dict and encodes their keys, if any, to ascii.
    :param d:
    :return:
    """
    new_d = _decode(d)
    for key in new_d:
        if isinstance(new_d[key], dict):
            dec= _decode(new_d[key])
            new_d[key] = recursive_decode(dec)
        elif isinstance(new_d[key], list):
            new_d[key] = _decode_list(new_d[key])
        else:
            continue
    return new_dlocalbitcoins


def median(seq):
    """
    Finds the median of a squence
    :param seq:
    :return:
    """
    seq.sort()
    if len(seq) % 2 is not 0: #uneven number of elements
        return seq[len(seq) / 2 + (len(seq) % 2)]
    else:
        return (seq[len(seq)/2] + seq[len(seq)+1] / 2)


def mean(seq):
    """
    finds the mean of a given list
    :param seq:
    :return:
    """
    return sum(seq) / len(seq)


def variance(seq):
    """
    Finds the variance of a given list
    :param seq:
    :return:
    """
    mean = mean(seq) # find mean of list
    a = [ (x-mean)**2 for x in seq] #substract mean from each num and square
    return mean(a) #return mean of a


def stan_dev(seq):
    """
    finds the standard deviation of a given list
    :param seq:
    :return:
    """
    return math.sqrt(variance(seq))
