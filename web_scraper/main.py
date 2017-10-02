import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
import requests
from web_scraper.cli import cli_parser
from web_scraper.core import scrapers, html_fetchers, prettifiers, file_handlers, task_handlers


def _scrape(url, target, target_type, specific_tag, regex, user_agent, filename,
	path, dont_save, keep_tags):
	"""Scrape data and return it"""
	status_code, html_document = html_fetchers.fetch_html_document(url, user_agent=user_agent)
	
	if status_code == requests.codes.ok:
		scraped_data = scrapers.scrape_target_elements(html_document, target=target,
			target_type=target_type,
			specific_tag=specific_tag
		)

		if not keep_tags or keep_tags == 'False':
			scraped_data = prettifiers.remove_html_tags(scraped_data)

		if regex:
			scraped_data = prettifiers.regex_prettifier(scraped_data, regex)

		if dont_save is True or dont_save == 'True':
			for data in scraped_data:
				logging.info(data)
		else:
			created_file_path = file_handlers.save_data_to_file(scraped_data,
				filename=filename,
				location=path
			)
			logging.info(f'Data saved to {created_file_path}')
	else:
		logging.info(f'We did not recieve a status code of 200. Instead we got: {status_code}.')


def _run_task(task):
	_scrape(task['url'], task['target'], task['target_type'], task['tag'],
		task['regex'], task['user_agent'], task['filename'], task['path'],
		task['dont_save'], task['keep_tags']
	)


def _log_task(task):
	for column, value in task.items():
		logging.info(f'{column}: {value}')
	logging.info('\n')


def main(args):
	logging.basicConfig(level=args.loglevel or logging.INFO, format='%(message)s')

	logging.debug(f'Starting the script...')

	if args.command == 'scrape':
		logging.debug(f'Scraping data from {args.url}...')
		_scrape(args.url, args.target, args.target_type,
			args.tag, args.exp, args.agent, args.fname, args.path,
			args.dont_save, args.keep_tags
		)
	
	elif args.command == 'create_task':
		logging.debug(f'Creating a task for you...')
		task_handlers.create_task(args.name, args.url, args.target, args.target_type,
			task_group=args.group, tag=args.tag, keep_tags=args.keep_tags,
			regex=args.exp, user_agent=args.agent, filename=args.fname,
			path=args.path, dont_save=args.dont_save
		)

	elif args.command == 'remove_task':
		logging.debug(f'Removing task {args.task}...')
		task_handlers.remove_task(args.task)

	elif args.command == 'show_task':
		if args.task == 'all':
			tasks = task_handlers.return_task(all_tasks=True)
			if tasks:
				logging.debug(f'Running task(s) for you...')
				for task in tasks:
					_log_task(task)
			else:
				logging.warn('No tasks exists!')

		elif args.task == 'group':
			tasks = task_handlers.return_task(task_group=args.name)
			if tasks:
				logging.debug(f'Running task(s) for you...')
				for task in tasks:
					_log_task(task)
			else:
				logging.warn(f'No such group ({args.name}) exists!')
		elif args.task == 'name':
			task = task_handlers.return_task(task_name=args.name)
			if task:
				_log_task(task)
			else:
				logging.warn(f'That task ({args.name}) does not exist!')
	
	elif args.command == 'run_task':
		if args.task == 'all':
			tasks = task_handlers.return_task(all_tasks=True)
			if tasks:
				logging.debug(f'Running task(s) for you...')
				for task in tasks:
					logging.debug('Current task: {}'.format(task['task_name']))
					_run_task(task)
			else:
				logging.warn('No tasks exists!')

		elif args.task == 'group':
			tasks = task_handlers.return_task(task_group=args.name)
			if tasks:
				logging.debug(f'Running task(s) for you...')
				for task in tasks:
					logging.debug('Current task: {}'.format(task['task_name']))
					_run_task(task)
			else:
				logging.warn(f'No such group ({args.name}) exists!')
		elif args.task == 'name':
			task = task_handlers.return_task(task_name=args.name)
			if task:
				logging.debug(f'Running task for you...')
				_run_task(task)
			else:
				logging.warn(f'That task ({args.name}) does not exist!')


if __name__ == '__main__':
	args = cli_parser.parse_options()
	main(args)
