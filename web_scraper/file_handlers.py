import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random


def save_data_to_file(data, filename='data', location='./'):
    """Return true if data has been saved to file

    :param list data: a list that contains data
    :param str filename: the desired filename
    :param str location: the desired location for the data file
    :return: file location
    :rtype: str
    """
    filename = f'{filename}_{random.randint(10000, 50000)}.txt'
    while os.path.isfile(filename):
        filename = f'{filename}_{random.randint(10000, 50000)}.txt'

    with open(f'{location}{filename}', 'w') as data_file:
        for item in data:
            data_file.write(f'{item}\n')
    return f'{location}\\{filename}'


def read_file_into_list(file_location):
    """Return list of elements from file

    :param str file_location: location of the file containing the proxies
    :return: list of elements from file
    :rtype: list
    """
    return_list = []

    with open(file_location, 'r') as File:
        for line in File:
            line = line.strip()
            proxies.append(line)

    return return_list

