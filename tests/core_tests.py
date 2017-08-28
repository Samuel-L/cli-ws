import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests import helpers
from tests import test_elements

from web_scraper import core


class TestFetchHtmlDocumenthMethod(unittest.TestCase):
    """Test fetch_html_document(url) method"""
    def test_html_fetch(self):
        """method should return html of page"""
        url = 'http://motherfuckingwebsite.com/'
        self.assertEqual((200, helpers.fetch_local_html('200status')), core.fetch_html_document(url))

    def test_404_url(self):
        """method should return status code if 404 (file not found)"""
        url = 'http://motherfuckingwebsite.com/ke'
        self.assertEqual((404, helpers.fetch_local_html('404status')), core.fetch_html_document(url))


class TestScrapeTargetElementsMethod(unittest.TestCase):
    """Test target_fetch(html, target)"""
    def setUp(self):
        self.html_changed = helpers.fetch_local_html('200status_changed')
        self.html_normal = helpers.fetch_local_html('200status')
        self.element = 'li'
        self.class_name = 'test-class'
        self.id_name = 'test-id'

    def test_scrape_by_tag(self):
        """method should return all li elements"""
        scrape_target_elements = core.scrape_target_elements(
            self.html_normal,
            target=self.element,
            target_type='tag'
        )
        self.assertEqual(test_elements.li_elements, str(scrape_target_elements))

    def test_scrape_by_class_name(self):
        """method should return all elements with the class 'test-class'"""
        scrape_target_elements = core.scrape_target_elements(
            self.html_changed,
            target=self.class_name,
            target_type='class'
        )
        self.assertEqual(test_elements.class_elements, str(scrape_target_elements))

    def test_scrape_by_id(self):
        """method should return elements with the id 'test-id'"""
        scrape_target_elements = core.scrape_target_elements(
            self.html_changed,
            target=self.id_name,
            target_type='id'
        )
        self.assertEqual(test_elements.id_elements, str(scrape_target_elements))

    def test_scrape_by_class_name_and_tag(self):
        """method should return all elements with the class 'test-class' and 'h2' tag"""
        scrape_target_elements = core.scrape_target_elements(
            self.html_changed,
            target=self.class_name,
            target_type='class',
            specific_tag='h2'
        )
        self.assertEqual(test_elements.tag_specific_class_elements, str(scrape_target_elements))

    def test_scrape_by_id_and_tag(self):
        """method should return all elements with the 'test-id' id and 'h2' tag"""
        scrape_target_elements = core.scrape_target_elements(
            self.html_changed,
            target=self.id_name,
            target_type='id',
            specific_tag='h2'
        )
        self.assertEqual(test_elements.tag_specific_id_elements, str(scrape_target_elements))


class TestSaveDataToFile(unittest.TestCase):
    """Test save_data_to_file()"""
    def setUp(self):
        self.data = ['item1', 'item2', 'item3']
        filename = 'dataFile'
        self.created_file_location = core.save_data_to_file(self.data, filename=filename)

    def test_creates_file(self):
        """method should have created a file and returned its location"""
        file_exists = os.path.isfile(self.created_file_location)
        self.assertTrue(file_exists)

    def test_saved_data_is_correct(self):
        with open(self.created_file_location, 'r') as created_file:
            written_data = created_file.readlines()
        written_data = [item.rstrip('\n') for item in written_data]
        self.assertEqual(self.data, written_data)

    def tearDown(self):
        """remove the created data file"""
        os.remove(self.created_file_location)

if __name__ == '__main__':
    unittest.main()
