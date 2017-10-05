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
    """Prettify the scraped data using a regular expression

    Positional Arguments:
        scraped_data (list): data scraped from a website
        regex (str): a regular expression
    Return:
        list: the regex modified data
    """
    data_list = []
    for data in scraped_data:
        data_list.append(re.sub(regex, '', data))
    return data_list
