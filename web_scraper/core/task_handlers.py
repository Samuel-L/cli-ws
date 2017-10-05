import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv
import shutil


def _create_task_file(name):
	"""Creates a taskfile

	Positional Arguments:
		name (str): the name of the taskfile
	"""
	with open('taskfile.csv', 'w', newline='') as taskfile:
		writer = csv.writer(taskfile, delimiter=',', quotechar='"',
			quoting=csv.QUOTE_MINIMAL
		)
		
		writer.writerow(['task_name', 'url', 'target',
			'target_type', 'tag', 'keep_tags', 'regex', 
			'user_agent', 'filename', 'path', 'dont_save', 'task_group'
		])


def create_task(task_name, url, target, 
	target_type, task_group='', tag='',
	keep_tags='', regex='', user_agent='', filename='', path='', dont_save=''):
	"""Append a task to the taskfile

	Positional Arguments:
		task_name (str): the name of the task
		url (str): a web address (http://example.com/)
		target (str): name of tag, id or class
		target_type (str): tag (html element such as <li>, <p>), id or class
	Keyword Arguments:
		task_group (str): the group of tasks this task should be added to
		tag (str): if target_type is id or class, this keyword argument
            can be used to only scrape targets with this html tag
		keep_tags (bool): don't remove the html tags
		regex (str): a regular expression (applied after html tags has been removed)
		user_agent(str): use this agent when sending get request
		filename (str): the name of the file that will contain the 
		scraped data
		path (str): the path for the data file
		dont_save (bool): don't save the data to a file
	Return:
		Nothing
	"""
	if not os.path.isfile('taskfile.csv'):
		_create_task_file('taskfile.csv')

	with open('taskfile.csv', 'a', newline='') as taskfile:
		writer = csv.writer(taskfile, delimiter=',', quotechar='"',
			quoting=csv.QUOTE_NONNUMERIC
		)
		writer.writerow([task_name, url, target,
			target_type, tag, keep_tags, regex,
			user_agent, filename, path, dont_save, task_group
		])


def return_task(task_name='', task_group='', all_tasks=False):
	"""Return task

	Keyword Arguments:
		task_name (str): name of the task
		task_group (str): group name of one or more tasks
		all_tasks (bool): return all tasks
	Return:
		OrderedDict (task_name is used): the task that matches
			with that name
		list (task_group is used): all of the tasks that
			is that specific task_group
		list (all_tasks is used): all of the tasks in the taskfile
	"""
	with open('taskfile.csv', 'r') as taskfile:
		reader = csv.DictReader(taskfile)
		task_list = []

		if task_name:
			for task in reader:
				if task['task_name'] == task_name:
					return type(task)
			return False
		elif task_group:
			for task in reader:
				if task['task_group'] == task_group:
					task_list.append(task)
			return type(task_list)
		elif all_tasks:
			for task in reader:
				task_list.append(task)
			return type(task_list)
		else:
			return False


def remove_task(task_name):
	"""Remove the task
	:param str task_name: name of the task
	:return: true or false depending on if the task was removed
	:rtype: bool
	"""
	fieldnames = ['task_name', 'url', 'target', 'target_type',
		'tag', 'keep_tags', 'regex', 'user_agent','filename',
		'path', 'dont_save', 'task_group'
	]

	with open('taskfile.csv', 'r') as taskfile, open('output.csv', 'w') as outfile:
		reader = csv.DictReader(taskfile, fieldnames=fieldnames)
		writer = csv.writer(outfile)

		for row in reader:
			if not task_name in row['task_name']:
				writer.writerow([row['task_name'], row['url'], row['target'],
					row['target_type'], row['tag'], row['keep_tags'],
					row['regex'], row['user_agent'], row['filename'], row['path'],
					row['dont_save'], row['task_group']
				])
	shutil.move('output.csv','taskfile.csv')
