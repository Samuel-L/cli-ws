import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests import helpers
from li_elements import li_elements
from web_scraper import core


class TestHtmlFetchMethod(unittest.TestCase):
    """Test html_fetch(url) method"""
    def test_html_fetch(self):
        """method should return html of page"""
        url = 'http://motherfuckingwebsite.com/'
        self.assertEqual((200, helpers.fetch_local_html('200status')), core.html_fetch(url))
    def test_404_url(self):
        """method should return status code if 404 (file not found)"""
        url = 'http://motherfuckingwebsite.com/ke'
        self.assertEqual((404, helpers.fetch_local_html('404status')), core.html_fetch(url))


class TestTargetFetchMethod(unittest.TestCase):
    """Test target_fetch(html, target)"""
    def test_target_fetch_li_elements(self):
        """method should return all li elements from html"""
        html = helpers.fetch_local_html('200status')
        self.assertEqual(li_elements, core.target_fetch(html, 'li'))

if __name__ == '__main__':
    unittest.main()