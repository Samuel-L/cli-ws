import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bs4 import BeautifulSoup


def scrape_multiple_elements(html, targets):
    """Scrape multiple elements from the html document
    
    Positional Arguments:
        html (str): standard html document
        targets (dict): contains the target, target type and specific tag
            ex: {
                1: {'target': '', 'target_type': '', 'specific_tag': ''}
                2: {'target': '', 'target_type': '', 'specific_tag': ''}
                }
    Return:
        list: all of the scraped elements from the html document
    """
    scraped_elements = []

    for key, target in targets.items():
        element = target['target']
        element_type = target['target_type']
        specific_tag = target['specific_tag']

        scraped_element = scrape_target_elements(html,
            target=element,
            target_type=element_type,
            specific_tag=specific_tag
        )

        scraped_elements.append(scraped_element)

    return scraped_elements


def scrape_target_elements(html, target, target_type, specific_tag=''):
    """Scrape target from the html document
    
    Positional Arguments:
        html (str): standard html document
        target (str): name of tag, id or class
        target_type (str): tag (html element such as <li>, <p>), id or class
    Keyword Arguments:
        specific_tag (str): if target_type is id or class, this keyword argument
            can be used to only scrape targets with this html tag
    Return:
        bs4.element.ResultSet: all scraped targets
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
