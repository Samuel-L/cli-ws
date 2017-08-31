import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bs4 import BeautifulSoup


def scrape_target_elements(html, target, target_type, specific_tag=''):
    """Scrape the target from the html

    :param str html: standard html document
    :param str target: name of tag, id or class
    :param str target_type: tag (html element such as <li>, <p>), id or class
    :param str specific_tag: (optional) if target_type is id or class, this argument
    can be used to only scrape targets with this html tag
    :return: all scraped targets
    :rtype: bs4.element.ResultSet
    """
    soup = BeautifulSoup(html, 'html.parser')
    if target_type == 'tag':
        return soup.find_all(target)
    else:
        return soup.find_all(specific_tag, attrs={target_type: target})


def scrape_links(domain_name, html):
    """Scrape all links from the html

    :param str domain_name: the domain name of the website you're scraping
    :param str html: standard html document
    :return: all scraped links
    :rtype: list
    """
    soup = BeautifulSoup(str(html), 'html.parser')
    link_list = []
    for link in soup.find_all('a'):
        link = link.get('href')

        # If link only includes a path to a page on the website (internal link),
        # add the domain name here.
        if domain_name not in link:
            link = f'{domain_name}{link}'

        link_list.append(link)

    return link_list
