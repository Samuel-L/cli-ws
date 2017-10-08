import os, errno
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random


def create_documents_folder():
    """Create a folder in the users documents folder that will
    hold the config file, scraped data and taskfile.

    Return:
        str: path to created folder
    """
    documents_folder_path = os.path.expanduser('~/Documents')
    try:
        os.makedirs(f'{documents_folder_path}/cli_ws_1.0.0')
        os.makedirs(f'{documents_folder_path}/cli_ws_1.0.0/scraped_data')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    finally:
        return f'{documents_folder_path}/cli_ws_1.0.0'


def save_data_to_existing_file(data, file):
    """Save data to existing file

     Positional Arguments:
        data (list): list of data
        file (str): full path to file
     Return:
        tuple (sucess): (True, complete path to file)
        tuple (failure): (False, empty string)
    """
    if os.path.isfile(file):
        with open(file, 'a') as data_file:
            for item in data:
                data_file.write(f'{item}\n')
        return (True, file)
    else:
        return (False, '')


def save_data_to_new_file(data, filename='data'):
    """Save data to new file

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

    full_path = os.path.expanduser(f'~/Documents/cli_ws_1.0.0/scraped_data/{filename}')
    with open(full_path, 'w') as data_file:
        for item in data:
            data_file.write(f'{item}\n')

    return full_path


def read_file_into_list(file_location):
    """Return list of elements from file

    Positional Arguments:
        file_location (str): location of the file containing the data
    Return:
        list: everything from the file
    """
    return_list = []

    with open(file_location, 'r') as File:
        for line in File:
            line = line.strip()
            return_list.append(line)

    return return_list
