import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests import helpers
from tests import test_elements

from web_scraper import scrapers


class TestScrapeMultipleElementsMethod(unittest.TestCase):
    """Test scrape_multiple_elements(html, targets)"""
    def setUp(self):
        self.html = helpers.fetch_local_html('200status')
        self.targets = {
            1: {'target': 'h1', 'target_type': 'tag', 'specific_tag': ''},
            2: {'target': 'h2', 'target_type': 'tag', 'specific_tag': ''}
        }
    def test_scrape_multiple_elements(self):
        self.assertEqual(
            test_elements.multiple_scraped_targets,
            str(scrapers.scrape_multiple_elements(self.html, self.targets))
        )


class TestScrapeTargetElementsMethod(unittest.TestCase):
    """Test target_fetch(html, target)"""
    def setUp(self):
        self.html_changed = helpers.fetch_local_html('200status_changed')
        self.html_normal = helpers.fetch_local_html('200status')
        self.element = 'li'
        self.class_name = 'test-class'
        self.id_name = 'test-id'

    def test_scrape_by_tag(self):
        """method should return all li elements"""
        scrape_target_elements = scrapers.scrape_target_elements(
            self.html_normal,
            target=self.element,
            target_type='tag'
        )
        self.assertEqual(test_elements.li_elements, str(scrape_target_elements))

    def test_scrape_by_class_name(self):
        """method should return all elements with the class 'test-class'"""
        scrape_target_elements = scrapers.scrape_target_elements(
            self.html_changed,
            target=self.class_name,
            target_type='class'
        )
        self.assertEqual(test_elements.class_elements, str(scrape_target_elements))

    def test_scrape_by_id(self):
        """method should return elements with the id 'test-id'"""
        scrape_target_elements = scrapers.scrape_target_elements(
            self.html_changed,
            target=self.id_name,
            target_type='id'
        )
        self.assertEqual(test_elements.id_elements, str(scrape_target_elements))

    def test_scrape_by_class_name_and_tag(self):
        """method should return all elements with the class 'test-class' and 'h2' tag"""
        scrape_target_elements = scrapers.scrape_target_elements(
            self.html_changed,
            target=self.class_name,
            target_type='class',
            specific_tag='h2'
        )
        self.assertEqual(test_elements.tag_specific_class_elements, str(scrape_target_elements))

    def test_scrape_by_id_and_tag(self):
        """method should return all elements with the 'test-id' id and 'h2' tag"""
        scrape_target_elements = scrapers.scrape_target_elements(
            self.html_changed,
            target=self.id_name,
            target_type='id',
            specific_tag='h2'
        )
        self.assertEqual(test_elements.tag_specific_id_elements, str(scrape_target_elements))


class TestLinkScraper(unittest.TestCase):
    """Test scrape_links()"""
    def test_scrapes_links(self):
        """method should return all links (list) with the domain name included"""
        link_list = scrapers.scrape_links(
            domain_name='https://github.com', html=test_elements.links
        )
        self.assertEqual(test_elements.links_list, link_list)


if __name__ == '__main__':
    unittest.main()