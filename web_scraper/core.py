import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from bs4 import BeautifulSoup

from web_scraper import target_types


def fetch_html_document(url):
    """Fetch html from url and return html

    :param str url: an address to a resource on the Internet
    :return no except hit: status code and html of page (if exists)
    :rtype: tuple
    :return except hit: error
    :rtype: str
    """
    try:
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            return response.status_code, response.text # html
        else:
            return response.status_code, response.text
    except Exception as err:
        return err


def scrape_target_elements(html, target, target_type, specific_tag=''):
    """Fetch the target from the html

    :param str html: standard html
    :param str target: a html element, id, or class
    :param str target_type: tag (html element such as <li>, <p>), id or class
    :param str specific_tag: if target_type is id or class, this optional argument
    can be used to only fetch targets with this html tag
    :return: all fetched targets
    :rtype: str
    """
    soup = BeautifulSoup(str(html), 'html.parser')
    if target_type == target_types.TAG:
        return str(soup.find_all(target))
    else:
        return str(soup.find_all(specific_tag, attrs={target_type: target}))


if __name__ == '__main__':
    pass
