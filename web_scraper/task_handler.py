import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv

def _create_task_file(name):
	"""Create a taskfile
	:param str name: the name of the taskfile
	"""
	with open('taskfile.csv', 'w', newline='') as taskfile:
		writer = csv.writer(taskfile, delimiter=',', quotechar='"',
			quoting=csv.QUOTE_MINIMAL
		)
		
		writer.writerow(['task_name', 'url', 'target',
			'target_type', 'specific_tag', 'no_prettify', 'regex',
			'filename', 'path', 'dont_save', 'task_group'
		])


def create_task(task_name, url, target, 
	target_type, task_group='', specific_tag='',
	no_prettify='', regex='', filename='', path='', dont_save=''):
	"""Append a task to the taskfile

	:param str task_name: the name of the task
	:param str url: a standard website url
	:param str target: the target for scraping
	:param str target_type: the type of target (tag, class or id)
	:opt param str task_group: the group of tasks this task should be added to
	:opt param str specific_tag: only scrape data from this tag
	:opt param bool no_prettify: don't apply the simple prettifer
	:opt param str regex: apply this regex after the simple prettifier
	:opt param str filename: the name of the file that will contain the 
	scraped data
	:opt param str path: the path for the data file
	:opt param bool dont_save: don't save the data to a file
	"""
	if not os.path.isfile(f'{task_file}.taskfile.csv'):
		_create_task_file(task_file)

	with open('taskfile.csv', 'a', newline='') as taskfile:
		writer = csv.writer(taskfile, delimiter=',', quotechar='"',
			quoting=csv.QUOTE_NONNUMERIC
		)
		writer.writerow([task_name, url, target,
			target_type, specific_tag, no_prettify, regex,
			filename, path, dont_save, task_group
		])

def return_task(task_name):
	"""Return the task
	:param str task_name: name of the task
	:return: the task or False
	:rtype: OrderedDict or bool
	"""
	with open('taskfile.csv', 'r') as taskfile:
		reader = csv.DictReader(taskfile)

		for task in reader:
			if task['task_name'] == task_name:
				return task

		return False
