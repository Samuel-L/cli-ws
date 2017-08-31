import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests import test_elements

from web_scraper import file_handlers


class TestSaveDataToFile(unittest.TestCase):
    """Test save_data_to_file()"""
    def setUp(self):
        self.data = ['item1', 'item2', 'item3']
        filename = 'dataFile'
        self.created_file_location = file_handlers.save_data_to_file(
            self.data,
            filename=filename
        )

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