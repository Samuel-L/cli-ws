import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.test_files import html_doc


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
		return MockResponse(200, (200, html_doc.doc))
	
	return MockResponse(404, (404, 'Not Found'))


def return_html_document():
	"""Return the 'github-python-trending' html document"""
	with open('tests/test_files/html-document.html', 'r') as html_file:
		html_document = html_file.read()
	return html_document
