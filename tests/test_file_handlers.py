import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from unittest import mock

from web_scraper.core import file_handlers


def mocked_random_randint(*args, **kwargs):
	"""this method will be used by the mock to replace random.randint"""
	return 1

class TestSaveDataToExistingFile(unittest.TestCase):
	def setUp(self):
		self.scraped_data_folder = file_handlers.create_documents_folder()
		self.scraped_data_folder += '/scraped_data'

		with open(f'{self.scraped_data_folder}/data.txt', 'w') as data_file:
			data_file.write('first\n')

	def test_appends_to_exisiting_file(self):
		status, path = file_handlers.save_data_to_existing_file(['test_data'],
			f'{self.scraped_data_folder}/data.txt')

		with open(f'{self.scraped_data_folder}/data.txt', 'r') as data_file:
			entire_file = data_file.read()

		self.assertTrue(status)
		self.assertTrue(os.path.isfile(path))
		self.assertTrue('test_data' in entire_file)

	def tearDown(self):
		os.remove(f'{self.scraped_data_folder}/data.txt')


class TestSaveDataToNewFileFunction(unittest.TestCase):
	def setUp(self):
		self.path_to_document_folder = file_handlers.create_documents_folder()
		self.data = ['hello world']

	@mock.patch('web_scraper.core.file_handlers.random.randint', side_effect=mocked_random_randint)
	def test_creates_a_file(self, mock_random):
		"""save_data_to_new_file creates a file"""
		file_handlers.save_data_to_new_file(self.data)
		self.assertTrue(os.path.isfile(f'{self.path_to_document_folder}/scraped_data/data_1.csv'))

	@mock.patch('web_scraper.core.file_handlers.random.randint', side_effect=mocked_random_randint)
	def test_saves_data_to_file(self, mock_random):
		"""save_data_to_new_file saves data to created file"""
		file_handlers.save_data_to_new_file(self.data)
		with open(f'{self.path_to_document_folder}/scraped_data/data_1.csv', 'r') as test_file:
			data_from_file = test_file.read().replace('\n', '')
		self.assertEqual('hello world', data_from_file)

	@mock.patch('web_scraper.core.file_handlers.random.randint', side_effect=mocked_random_randint)
	def test_returns_location_of_created_file(self, mock_random):
		"""save_data_to_new_file returns the location of the created file"""
		path = file_handlers.save_data_to_new_file(self.data)
		self.assertEqual(f'{self.path_to_document_folder}/scraped_data/data_1.csv', path)

	@mock.patch('web_scraper.core.file_handlers.random.randint', side_effect=mocked_random_randint)
	def test_takes_user_inputted_filename(self, mock_random):
		"""save_data_to_new_file uses the filename given by the user when creating the file"""
		filename = 'my_data'
		file_handlers.save_data_to_new_file(self.data, filename=filename)
		self.assertTrue(os.path.isfile(f'{self.path_to_document_folder}/scraped_data/my_data_1.csv'))

	def tearDown(self):
		if os.path.isfile(f'{self.path_to_document_folder}/scraped_data/my_data_1.csv'):
			file = f'{self.path_to_document_folder}/scraped_data/my_data_1.csv'
		elif os.path.isfile(f'{self.path_to_document_folder}/scraped_data/data_1.csv'):
			file = f'{self.path_to_document_folder}/scraped_data/data_1.csv'
		os.remove(file)


if __name__ == '__main__':
	unittest.main()
