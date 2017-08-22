import requests
from bs4 import BeautifulSoup


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

def target_fetch(html, target):
    """Fetch the target from the html

    :param str html: standard html
    :param str target: a html element, id, or class
    :return: all fetched targets or not found
    :rtype: str
    """
    soup = BeautifulSoup(str(html), 'html.parser')
    return str(soup.find_all(target))



if __name__ == '__main__':
    print(target_fetch(html_fetch('http://motherfuckingwebsite.com/'), 'li'))
