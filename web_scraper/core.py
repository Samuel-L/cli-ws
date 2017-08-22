import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from bs4 import BeautifulSoup

from web_scraper import target_types as tt

def html_fetch(url):
    """Fetch html from url and return html

    :param str url: an address to a resource on the Internet
    :return no except hit: status code and html of page (if exists)
    :rtype: tuple
    :return except hit: error
    :rtype: str
    """
    try:
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            return res.status_code, res.text # html
        else:
            return res.status_code, res.text
    except Exception as err:
        return err

def target_fetch(html, target, target_type):
    """Fetch the target from the html

    :param str html: standard html
    :param str target: a html element, id, or class
    :param str target_type: standard (html element such as <li>, <p>), id or class
    :return: all fetched targets or not found
    :rtype: str
    """
    soup = BeautifulSoup(str(html), 'html.parser')
    if target_type == tt.TAG:
        return str(soup.find_all(target))
    else:
        return str(soup.find_all(attrs={target_type: target}))


if __name__ == '__main__':
    pass