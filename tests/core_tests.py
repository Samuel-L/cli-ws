import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests import helpers
import test_elements as te

from web_scraper import core
from web_scraper import target_types as tt

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
    def setUp(self):
        self.html_changed = helpers.fetch_local_html('200status_changed')
        self.html_normal = helpers.fetch_local_html('200status')
        self.element = 'li'
        self.class_name = 'test-class'
        self.id_name = 'test-id'
    def test_target_fetch_li_elements(self):
        """method should return all li elements from html"""
        self.assertEqual(te.li_elements, core.target_fetch(self.html_normal, target=self.element, target_type=tt.TAG))
    def test_target_fetch_class_elements(self):
        """method should return all class (specific class) elements from html"""
        self.assertEqual(te.class_elements, core.target_fetch(self.html_changed, target=self.class_name, target_type=tt.CLASS))
    def test_target_fetch_id_elements(self):
        """method should return all id (specific id) elements from html"""
        self.assertEqual(te.id_elements, core.target_fetch(self.html_changed, target=self.id_name, target_type=tt.ID))
    def test_target_fetch_tag_specific_class_elements(self):
        """method should return all class (specific class and tag) elements from html"""
        self.assertEqual(te.tag_specific_class_elements, core.target_fetch(self.html_changed, target=self.class_name, target_type=tt.CLASS, specific_tag='h2'))
        

if __name__ == '__main__':
    unittest.main()