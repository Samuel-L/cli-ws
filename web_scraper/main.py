import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from web_scraper.cli import cli_parser, scraper, task
from web_scraper.core import task_handlers


def main(args):
	logging.basicConfig(level=args.loglevel or logging.INFO, format='%(message)s')

	logging.debug(f'Starting the script...')

	if args.command == 'scrape':
		scraper.scrape(args.url, args.target, args.target_type,
			args.tag, args.exp, args.agent, args.fname, args.path,
			args.dont_save, args.keep_tags
		)
	
	elif args.command == 'create_task':
		task.create(args)

	elif args.command == 'remove_task':
		task.remove(args)

	elif args.command == 'show_task':
		task.show(args)
	
	elif args.command == 'run_task':
		task.run(args)


if __name__ == '__main__':
	args = cli_parser.parse_options()
	main(args)
