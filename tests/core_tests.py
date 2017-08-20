import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from requests.exceptions import ConnectionError

from tests import helpers
from web_scraper import core


class TestReturnHtmlMethod(unittest.TestCase):
    """Test all core methods"""
    def test_return_html(self):
        """method should return html of page"""
        url = 'http://motherfuckingwebsite.com/'
        self.assertEqual(helpers.fetch_local_html(), core.return_html(url))
    def test_404_url(self):
        """method should return status code if 404 (file not found)"""
        url = 'http://motherfuckingwebsite.com/doesnotexist'
        self.assertEqual(404, core.return_html(url))
    def test_faulty_url(self):
        """method should return bad url error if url is faulty"""
        url = 'http://www.dkmawdjodiw.com/'
        self.assertEqual(
            f'INVALID URL: {url} does not exist!',
            core.return_html(url)
        )
    def test_missing_schema_url(self):
        """method should return 'missing schema' if url misses it"""
        url = 'dkmawdjodiw.com/'
        self.assertEqual(
            f'INVALID URL: {url} misses schema! Did you mean: http://{url}',
            core.return_html(url)
        )


if __name__ == '__main__':
    unittest.main()