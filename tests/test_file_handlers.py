import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest import mock

from web_scraper.core import file_handlers

def mocked_random_randint(*args, **kwargs):
	"""this method will be used by the mock to replace random.randint"""
	return 1


class TestSaveDataToFileFunction(unittest.TestCase):
	def setUp(self):
		self.data = ['hello world']
	
	@mock.patch('web_scraper.core.file_handlers.random.randint', side_effect=mocked_random_randint)
	def test_creates_a_file(self, mock_random):
		"""save_data_to_file creates a file"""
		file_handlers.save_data_to_file(self.data)
		self.assertTrue(os.path.isfile('./data_1.csv'))

	@mock.patch('web_scraper.core.file_handlers.random.randint', side_effect=mocked_random_randint)
	def test_saves_data_to_file(self, mock_random):
		"""save_data_to_file saves data to created file"""
		file_handlers.save_data_to_file(self.data)
		with open('./data_1.csv', 'r') as test_file:
			data_from_file = test_file.read().replace('\n', '')
		self.assertEqual('hello world', data_from_file)

	@mock.patch('web_scraper.core.file_handlers.random.randint', side_effect=mocked_random_randint)
	def test_returns_location_of_created_file(self, mock_random):
		"""save_data_to_file returns the location of the created file"""
		path = file_handlers.save_data_to_file(self.data)
		self.assertEqual(os.path.abspath('./data_1.csv'), path)

	@mock.patch('web_scraper.core.file_handlers.random.randint', side_effect=mocked_random_randint)
	def test_takes_user_inputted_filename(self, mock_random):
		"""save_data_to_file uses the filename given by the user when creating the file"""
		filename = 'my_data'
		file_handlers.save_data_to_file(self.data, filename=filename)
		self.assertTrue(os.path.isfile('./my_data_1.csv'))

	def tearDown(self):
		if os.path.isfile('./my_data_1.csv'):
			file = './my_data_1.csv'
		elif os.path.isfile('./data_1.csv'):
			file = './data_1.csv'
		
		os.remove(file)


if __name__ == '__main__':
	unittest.main()