import requests
from requests.exceptions import ConnectionError, MissingSchema

def return_html(url):
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


if __name__ == '__main__':
    pass
