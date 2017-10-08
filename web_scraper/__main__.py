import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from web_scraper.cli import cli_parser, scraper, task
from web_scraper.core import task_handlers, file_handlers


def main():
	documents_folder_path = os.path.expanduser('~/Documents/cli_ws_1.0.0')
	if not os.path.isdir(documents_folder_path):
		file_handlers.create_documents_folder()

	args = cli_parser.parse_options()

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
	main()
