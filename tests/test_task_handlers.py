import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from web_scraper.core import task_handlers


class TestCreateTaskFunction(unittest.TestCase):
	def setUp(self):
		self.documents_folder_path = os.path.expanduser('~/Documents/cli_ws_1.0.0')
		task_handlers.create_task('task name', 'website url', 'target', 'target type')

	def test_creates_a_file_if_none_exists(self):
		self.assertTrue(os.path.isfile(f'{self.documents_folder_path}/taskfile.csv'))

	def test_creates_a_file_with_correct_column_names(self):
		with open(f'{self.documents_folder_path}/taskfile.csv' , 'r') as taskfile:
			entire_file = taskfile.read()
			self.assertTrue('task_name,url,target,target_type,tag,keep_tags,regex,user_agent,filename,path,dont_save,task_group' in entire_file)

	def test_saves_task_to_file(self):
		with open(f'{self.documents_folder_path}/taskfile.csv', 'r') as taskfile:
			entire_file = taskfile.read()
			self.assertTrue('"task name","website url","target","target type","","","","","","","",""' in entire_file)

	def test_saves_consecutive_tasks_in_already_created_file(self):
		task_handlers.create_task('second task', 'website url', 'target', 'target type')

		with open(f'{self.documents_folder_path}/taskfile.csv', 'r') as taskfile:
			entire_file = taskfile.read()
			self.assertTrue('"task name","website url","target","target type","","","","","","","",""' in entire_file)
			self.assertTrue('"second task","website url","target","target type","","","","","","","",""' in entire_file)

	def tearDown(self):
		os.remove(f'{self.documents_folder_path}/taskfile.csv')


class TestReturnTaskFunction(unittest.TestCase):
	def setUp(self):
		self.documents_folder_path = os.path.expanduser('~/Documents/cli_ws_1.0.0')
		task_handlers.create_task('task name 1', 'website url', 'target', 'target type', task_group='a')
		task_handlers.create_task('task name 2', 'website url', 'target', 'target type', task_group='a')
		task_handlers.create_task('task name 3', 'website url', 'target', 'target type', task_group='b')
		task_handlers.create_task('task name 4', 'website url', 'target', 'target type', task_group='b')
		task_handlers.create_task('task name 5', 'website url', 'target', 'target type')

	def test_returns_task_by_name(self):
		task = task_handlers.return_task(task_name='task name 5')
		self.assertTrue('task name 5' in task['task_name'])

	def test_returns_task_by_group(self):
		task_group_a = task_handlers.return_task(task_group='a')
		self.assertTrue('task name 1' in task_group_a[0]['task_name'])
		self.assertTrue('task name 2' in task_group_a[1]['task_name'])

		task_group_b = task_handlers.return_task(task_group='b')
		self.assertTrue('task name 3' in task_group_b[0]['task_name'])
		self.assertTrue('task name 4' in task_group_b[1]['task_name'])

	def test_returns_all_tasks(self):
		all_tasks = task_handlers.return_task(all_tasks=True)
		task_names = ['task name 1', 'task name 2', 'task name 3', 'task name 4', 'task name 5']
		for task, name in zip(all_tasks, task_names):
			self.assertTrue(name in task['task_name'])

	def tearDown(self):
		os.remove(f'{self.documents_folder_path}/taskfile.csv')


class TestRemoveTaskFunction(unittest.TestCase):
	def setUp(self):
		self.documents_folder_path = os.path.expanduser('~/Documents/cli_ws_1.0.0')
		task_handlers.create_task('task name 1', 'website url', 'target', 'target type', task_group='a')
		task_handlers.create_task('task name 2', 'website url', 'target', 'target type', task_group='a')
		task_handlers.create_task('task name 3', 'website url', 'target', 'target type', task_group='b')
		task_handlers.create_task('task name 4', 'website url', 'target', 'target type', task_group='b')
		task_handlers.create_task('task name 5', 'website url', 'target', 'target type')

	def test_removes_task_by_name(self):
		task_handlers.remove_task('task name 1')
		with open(f'{self.documents_folder_path}/taskfile.csv', 'r') as taskfile:
			entire_file = taskfile.read()
			self.assertTrue('"task name 1"' not in entire_file)

	def tearDown(self):
		os.remove(f'{self.documents_folder_path}/taskfile.csv')


if __name__ == '__main__':
	unittest.main()
