import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests import helpers
from tests import test_elements

from web_scraper import html_fetchers


class TestFetchHtmlDocumenthMethod(unittest.TestCase):
    """Test fetch_html_document(url) method"""
    def test_html_fetch(self):
        """method should return html of page"""
        url = 'http://motherfuckingwebsite.com/'
        self.assertEqual((200, helpers.fetch_local_html('200status')), html_fetchers.fetch_html_document(url))

    def test_404_url(self):
        """method should return status code if 404 (file not found)"""
        url = 'http://motherfuckingwebsite.com/ke'
        self.assertEqual((404, helpers.fetch_local_html('404status')), html_fetchers.fetch_html_document(url))


if __name__ == '__main__':
    unittest.main()
