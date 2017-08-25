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
    """Scrape the target from the html

    :param str html: standard html document
    :param str target: name of tag, id or class
    :param str target_type: tag (html element such as <li>, <p>), id or class
    :param str specific_tag: (optional) if target_type is id or class, this argument
    can be used to only scrape targets with this html tag
    :return: all fetched targets
    :rtype: bs4.element.ResultSet
    """
    soup = BeautifulSoup(html, 'html.parser')
    if target_type == target_types.TAG:
        return soup.find_all(target)
    else:
        return soup.find_all(specific_tag, attrs={target_type: target})


if __name__ == '__main__':
    doc = fetch_html_document('http://motherfuckingwebsite.com/')
    data = scrape_target_elements(str(doc), target='li', target_type='tag')
    print(type(data))
