import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import re


def remove_html_tags(scraped_data):
    """Remove html tags from the scraped data

    Positional Arguments:
        scraped_data (bs4.element.ResultSet): data scraped from a website
    Return:
        list: the data without the html tags
    """
    data_list = []
    for data in scraped_data:
        data_list.append(data.text)
    return data_list


def regex_prettifier(scraped_data, regex):
    """Return regex modified data (in a list).

    :param list scraped_data: all the scraped data
    :param str regex: the regular expression you want to use to prettify the
    data
    :return: list of regex modified data
    :rtype: list
    """
    data_list = []
    for data in scraped_data:
        data_list.append(re.sub(regex, '', data))
    return data_list
