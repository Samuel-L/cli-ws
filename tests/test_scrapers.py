import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest

from web_scraper.core import scrapers
from tests import helpers
from tests.test_files import scraped_tags, scraped_classes, scraped_ids, scraped_class_specific_tag


class TestScrapeTargetElementsMethod(unittest.TestCase):
	def setUp(self):
		self.html_document = helpers.return_html_document()
		self.scraped_tags = scraped_tags.tag_elements
		self.scraped_classes = scraped_classes.class_elements
		self.scraped_ids = scraped_ids.id_elements
		self.scraped_specific = scraped_class_specific_tag.scraped_class_specific_tag

	def test_scrapes_by_tag(self):
		"""scrape_target_elements should return all elements with the tag 'h1'"""
		scraped_data = scrapers.scrape_target_elements(self.html_document, 'h1', 'tag')

		self.assertEqual(self.scraped_tags, str(scraped_data))

	def test_scrapes_by_class(self):
		"""scrape_target_elements should return all elements with the class 'class-name'"""
		scraped_data = scrapers.scrape_target_elements(self.html_document, 'class-name', 'class')

		self.assertEqual(self.scraped_classes, str(scraped_data))

	def test_scrapes_by_id(self):
		"""scrape_target_elements should return all elements with the id 'id-name'"""
		scraped_data = scrapers.scrape_target_elements(self.html_document, 'id-name', 'id')

		self.assertEqual(self.scraped_ids, str(scraped_data))

	def test_scrapes_by_class_and_specific_tag(self):
		"""scrape_target_elements should return all elements with the class 'class-name' and the specific tag 'p'"""
		scraped_data = scrapers.scrape_target_elements(self.html_document, 'class-name', 'class', specific_tag='p')

		self.assertEqual(self.scraped_specific, str(scraped_data))


if __name__ == '__main__':
	unittest.main()
