import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests


def fetch_html_document(url, user_agent='cli-ws/1.0'):
    """Request html document from url

    Positional Arguments:
        url (str): a web address (http://example.com/)
    Keyword Arguments:
        user_agent (str): the user agent that will be sent with the
            request (default: python_requests.cli-ws)
    Return:
        tuple: the status code of the response and the html document
    """
    response = requests.get(url, headers={'User-Agent': user_agent})
    
    return response.status_code, response.text

