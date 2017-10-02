import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from web_scraper.cli import cli_parser, scraper


def main(args):
	if args.command == 'scrape':
		scraper.scrape(args.url, args.target, args.target_type,
			args.tag, args.exp, args.agent, args.name, args.path,
			args.dont_save, args.keep_tags
		)


if __name__ == '__main__':
	args = cli_parser.parse_options()
	if args.loglevel:
		logging.basicConfig(level=args.loglevel, format='%(message)s')
	else:
		logging.basicConfig(level=logging.INFO, format='%(message)s')
	
	logging.debug(f'Starting the script {sys.argv[0]}...')

	main(args)
	