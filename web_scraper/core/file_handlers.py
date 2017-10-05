import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random


def save_data_to_file(data, filename='data', location='./'):
    """Save data to file
    
    Positional Arguments:
        data (list): list of data
    Keyword Arguments:
        filename (str): desired filename (default: data)
        location (str): location of the data file (default: ./)
    Return:
        str: complete filepath to file
    """
    filename = f'{filename}_{random.randint(10000, 50000)}.csv'
    while os.path.isfile(filename):
        filename = f'{filename}_{random.randint(10000, 50000)}.csv'

    with open(f'{location}{filename}', 'w') as data_file:
        for item in data:
            data_file.write(f'{item}\n')
    
    return os.path.abspath(f'{filename}')


def read_file_into_list(file_location):
    """Return list of elements from file

    :param str file_location: location of the file containing the data
    :return: list of elements from file
    :rtype: list
    """
    return_list = []

    with open(file_location, 'r') as File:
        for line in File:
            line = line.strip()
            return_list.append(line)

    return return_list
