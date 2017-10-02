import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import re


def remove_html_tags(scraped_data):
    """Return more presentable data (in a list) provided by scrape_target_elements()

    :param bs4.element.ResultSet scraped_data: all of the data scraped by scrape_target_elements()
    :return: list of presentable data
    :rtype: list
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
