import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import click

from web_scraper.core import task_handlers
from web_scraper.cli import helpers


@click.command()
@click.argument('task_name')
@click.argument('url')
@click.argument('target')
@click.argument('target_type', type=click.Choice(['tag', 'class', 'id']))
@click.option('--task-group', help='Name of the task group you want this task added to.')
@click.option('--no-prettify', is_flag=True, help='Returns the raw data. No prettifier applied.')
@click.option('--regex', help='Apply this regular expression after the simple prettifer.')
@click.option('--specific-tag', help='Only scrape data that uses this tag.')
@click.option('--filename', default='data', help='Save the file with this name.')
@click.option('--path', default='./', help='Save the file to this path.')
@click.option('--dont-save', is_flag=True, help='Don\'t save the data to a file, only output it.')
def create_task(task_name, url, target, target_type, task_group, no_prettify,
	regex, filename, path, dont_save, specific_tag):
	"""Create a task
	
	TASK_NAME name of the task

	URL         The url of the website you wish to scrape

	TARGET      The target that you wish to scrape from the website

	TARGET_TYPE The type of target you want to scrape (tag, class or id)
	"""
	task_handler.create_task(task_name, url, target, target_type,
		task_group=task_group, no_prettify=no_prettify, regex=regex, filename=filename,
		path=path, dont_save=dont_save)

	click.echo(f'Added task "{task_name}" to taskfile.csv')


@click.command()
@click.option('--run-all', is_flag=True, help='Run all tasks')
@click.option('--task-group', default=False, help='Run tasks from this group')
@click.option('--task-name', default=False, help='Run this task')
@click.pass_context
def run_task(ctx, run_all, task_group, task_name):
	"""Run a task

	Must choose one of the options down below.
	"""

	if run_all:
		tasks = task_handler.return_task(all_tasks=True)
		for task in tasks:
			helpers.invoke_scrape(ctx, task)
	elif task_group:
		tasks = task_handler.return_task(task_group=task_group)
		for task in tasks:
			helpers.invoke_scrape(ctx, task)
	elif task_name:
		task = task_handler.return_task(task_name=task_name)
		helpers.invoke_scrape(ctx, task)
	else:
		click.echo('You must choose one of the options!\n'
			'To view the options, type: cli-ws run_task --help'
		)


@click.command()
@click.argument('task_name')
def remove_task(task_name):
	"""Remove a task
	TASK_NAME name of task
	"""
	task_handler.remove_task(task_name)

	click.echo(f'Task "{task_name}" has been removed.')


@click.command()
@click.option('--show-all', is_flag=True, help='Show all tasks')
@click.option('--task-group', default=False, help='Show tasks from this group')
@click.option('--task-name', default=False, help='Show this task')
def show_task(show_all, task_group, task_name):
	""" Show task

	Must choose one of the options down below.
	"""

	if show_all:
		tasks = task_handler.return_task(all_tasks=True)
		for task in tasks:
			helpers.echo_task(task)
			click.echo('\n')
	elif task_group:
		tasks = task_handler.return_task(task_group=task_group)
		for task in tasks:
			helpers.echo_task(task)
			click.echo('\n')
	elif task_name:
		task = task_handler.return_task(task_name=task_name)
		helpers.echo_task(task)
		click.echo('\n')
	else:
		click.echo('You must choose one of the options!\n'
			'To view the options, type: cli-ws show_task --help'
		)
