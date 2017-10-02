import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests


def fetch_html_document(url, user_agent='python_requests.cli-ws'):
    """Fetch html from url and return html

    :param str url: an address to a resource on the Internet
    :opt param str user_agent: user agent that the request will be made with
    :return no except hit: status code and html of page (if exists)
    :rtype: tuple
    :return except hit: error
    :rtype: str
    """
    try:
        response = requests.get(url, headers={'User-Agent': user_agent})
        if response.status_code == requests.codes.ok:
            return response.status_code, response.text # html
        else:
            return response.status_code, response.text
    except Exception as err:
        return err
