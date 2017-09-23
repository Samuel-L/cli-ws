import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests


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
            return response.status_code, str(response.text) # html
        else:
            return response.status_code, str(response.text)
    except Exception as err:
        return err
