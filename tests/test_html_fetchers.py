import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest import mock

from web_scraper.core import html_fetchers


def mocked_requests_get(*args, **kwargs):
	"""this method will be used by the mock to replace requests.get"""
	class MockResponse:
		def __init__(self, html, status_code):
			self.html = html
			self.status_code = status_code

		def text(self):
			return self.html

		def status_code(self):
			return self.status_code

	if args[0] == 'http://example.com/':
		return MockResponse(200, (200, 'html'))
	
	return MockResponse(404, (404, 'Not Found'))


class TestFetchHtmlDocumentFunction(unittest.TestCase):
	@mock.patch('web_scraper.core.html_fetchers.requests.get', side_effect=mocked_requests_get)
	def test_returns_200_and_html(self, mock_get):
		"""fetch_html_document should return 200 and html"""
		response = html_fetchers.fetch_html_document('http://example.com/') # reponse = tuple, MockResponse object
		status_code = response[0][0]
		html = response[0][1]

		self.assertEqual((status_code, html), (200, 'html'))
	@mock.patch('web_scraper.core.html_fetchers.requests.get', side_effect=mocked_requests_get)
	def test_returns_404_and_not_found(self, mock_get):
		"""fetch_html_document should return 404 and 'Not Found'"""
		response = html_fetchers.fetch_html_document('http://example.com/nonexistantpath') # reponse = tuple, MockResponse object.
		status_code = response[0][0]
		html = response[0][1]

		self.assertEqual((status_code, html), (404, 'Not Found'))
		

if __name__ == '__main__':
	unittest.main()
