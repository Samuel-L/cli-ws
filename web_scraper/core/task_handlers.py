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

	:param str task_name: the name of the task
	:param str url: a standard website url
	:param str target: the target for scraping
	:param str target_type: the type of target (tag, class or id)
	:opt param str task_group: the group of tasks this task should be added to
	:opt param str tag: only scrape data from this tag
	:opt param bool keep_tags: don't apply the simple prettifer
	:opt param str regex: apply this regex after the simple prettifier
	:opt param str user_agent: use this agent when sending get request
	:opt param str filename: the name of the file that will contain the 
	scraped data
	:opt param str path: the path for the data file
	:opt param bool dont_save: don't save the data to a file
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
	"""Return the task
	:opt param str task_name: name of the task
	:opt param str task_group: group name of one or more tasks
	:opt param bool all_tasks: return all tasks
	:return: the task or False
	:rtype: OrderedDict or bool
	"""
	with open('taskfile.csv', 'r') as taskfile:
		reader = csv.DictReader(taskfile)
		task_list = []

		if task_name:
			for task in reader:
				if task['task_name'] == task_name:
					return task
			return False
		elif task_group:
			for task in reader:
				if task['task_group'] == task_group:
					task_list.append(task)
			return task_list
		elif all_tasks:
			for task in reader:
				task_list.append(task)
			return task_list
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
