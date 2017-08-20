import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests import helpers
from web_scraper import core


class TestCoreMethods(unittest.TestCase):
    """Test all core methods"""
    def test_return_html(self):
        """method should return html of page"""
        ok_url = 'http://motherfuckingwebsite.com/'
        self.assertEqual(helpers.fetch_local_html(), core.return_html(ok_url))
    def test_404_url(self):
        """method should return status code if 404 (file not found)"""
        fnf_url = 'http://motherfuckingwebsite.com/doesnotexist'
        self.assertEqual(404, core.return_html(fnf_url))
    def test_faulty_url(self):
        """method should return bad url error if url is faulty"""
        faulty_url = 'http://www.dkmawdjodiw.com/'
        self.assertEqual('bad url', core.return_html(faulty_url)) # USE BAD_URL ERROR


if __name__ == '__main__':
    unittest.main()