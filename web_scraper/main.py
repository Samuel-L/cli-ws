import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
import requests
from web_scraper.cli import cli_parser, helpers
from web_scraper.core import task_handlers


def main(args):
	logging.basicConfig(level=args.loglevel or logging.INFO, format='%(message)s')

	logging.debug(f'Starting the script...')

	if args.command == 'scrape':
		logging.debug(f'Scraping data from {args.url}...')
		helpers.scrape(args.url, args.target, args.target_type,
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
					helpers.log_task(task)
			else:
				logging.warn('No tasks exists!')

		elif args.task == 'group':
			tasks = task_handlers.return_task(task_group=args.name)
			if tasks:
				logging.debug(f'Running task(s) for you...')
				for task in tasks:
					helpers.log_task(task)
			else:
				logging.warn(f'No such group ({args.name}) exists!')
		elif args.task == 'name':
			task = task_handlers.return_task(task_name=args.name)
			if task:
				helpers.log_task(task)
			else:
				logging.warn(f'That task ({args.name}) does not exist!')
	
	elif args.command == 'run_task':
		if args.task == 'all':
			tasks = task_handlers.return_task(all_tasks=True)
			if tasks:
				logging.debug(f'Running task(s) for you...')
				for task in tasks:
					logging.debug('Current task: {}'.format(task['task_name']))
					helpers.run_task(task)
			else:
				logging.warn('No tasks exists!')

		elif args.task == 'group':
			tasks = task_handlers.return_task(task_group=args.name)
			if tasks:
				logging.debug(f'Running task(s) for you...')
				for task in tasks:
					logging.debug('Current task: {}'.format(task['task_name']))
					helpers.run_task(task)
			else:
				logging.warn(f'No such group ({args.name}) exists!')
		elif args.task == 'name':
			task = task_handlers.return_task(task_name=args.name)
			if task:
				logging.debug(f'Running task for you...')
				helpers.run_task(task)
			else:
				logging.warn(f'That task ({args.name}) does not exist!')


if __name__ == '__main__':
	args = cli_parser.parse_options()
	main(args)
