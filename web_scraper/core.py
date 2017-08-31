import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
import requests
from bs4 import BeautifulSoup


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


def prettify_scraped_data(scraped_data):
    """Return more presentable data (in a list) provided by scrape_target_elements()

    :param bs4.element.ResultSet scraped_data: all of the data scraped by scrape_target_elements()
    :return: list of presentable data
    :rtype: list
    """
    data_list = []
    for data in scraped_data:
        data_list.append(data.text)
    return data_list


def save_data_to_file(data, filename='data', location='./'):
    """Return true if data has been saved to file

    :param list data: a list that contains data
    :param str filename: the desired filename
    :param str location: the desired location for the data file
    :return: file location
    :rtype: str
    """
    filename = f'{filename}_{random.randint(10000, 50000)}.txt'
    while os.path.isfile(filename):
        filename = f'{filename}_{random.randint(10000, 50000)}.txt'
    
    with open(f'{location}{filename}', 'w') as data_file:
        for item in data:
            data_file.write(f'{item}\n')
    return f'{location}\\{filename}'


if __name__ == '__main__':
    pass 

