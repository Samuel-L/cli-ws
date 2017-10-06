import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest import mock

from web_scraper.core import html_fetchers
from tests import helpers
from tests.test_files import html_doc


class TestFetchHtmlDocumentFunction(unittest.TestCase):
	@mock.patch('web_scraper.core.html_fetchers.requests.get', side_effect=helpers.mocked_requests_get)
	def test_returns_200_and_html(self, mock_get):
		"""fetch_html_document should return 200 and html"""
		response = html_fetchers.fetch_html_document('http://example.com/') # reponse = tuple, MockResponse object
		status_code = response[0][0]
		html = response[0][1]

		self.assertEqual((status_code, html), (200, html_doc.doc))
	@mock.patch('web_scraper.core.html_fetchers.requests.get', side_effect=helpers.mocked_requests_get)
	def test_returns_404_and_not_found(self, mock_get):
		"""fetch_html_document should return 404 and 'Not Found'"""
		response = html_fetchers.fetch_html_document('http://example.com/nonexistantpath') # reponse = tuple, MockResponse object.
		status_code = response[0][0]
		html = response[0][1]

		self.assertEqual((status_code, html), (404, 'Not Found'))
		

if __name__ == '__main__':
	unittest.main()
