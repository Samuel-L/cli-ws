import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def simple_prettifier(scraped_data):
    """Return more presentable data (in a list) provided by scrape_target_elements()

    :param bs4.element.ResultSet scraped_data: all of the data scraped by scrape_target_elements()
    :return: list of presentable data
    :rtype: list
    """
    data_list = []
    for data in scraped_data:
        data_list.append(data.text)
    return data_list
