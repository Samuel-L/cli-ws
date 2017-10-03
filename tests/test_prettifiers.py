import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from bs4 import BeautifulSoup

from web_scraper.core import prettifiers


class TestRemoveHtmlTagsFunction(unittest.TestCase):
	def setUp(self):
		html = """<h1>H1 Tag</h1>, <h1 class="class-name">H1 Tag with class</h1>"""
		self.soup = BeautifulSoup(html, 'html.parser')

	def test_function_prettifies_data(self):
		"""remove_html_tags should return prettified data"""
		scraped_data = self.soup.find_all('h1')
		prettified_data = prettifiers.remove_html_tags(scraped_data)

		self.assertEqual(['H1 Tag', 'H1 Tag with class'], prettified_data)


class TestRegexPrettifierFunction(unittest.TestCase):
	def setUp(self):
		self.data = ["\\n      \\n        hello / world\\n "]

	def test_function_prettifies_data(self):
		"""regex prettifier should use regex to prettify the data"""
		regex_prettified_data = prettifiers.regex_prettifier(self.data, regex=r'\\n|\s+')
		self.assertEqual(['hello/world'], regex_prettified_data)


if __name__ == '__main__':
	unittest.main()