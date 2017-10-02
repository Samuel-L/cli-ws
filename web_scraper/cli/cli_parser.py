import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
import argparse


def parse_options():
	"""
	Parse all command line options and arguments and return them as a dictionary.
	"""
	parser = argparse.ArgumentParser(description='A web scraper for the command line')

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-v', '--verbose', dest='loglevel', help='increase output verbosity', action='store_const', const=logging.DEBUG)
	group.add_argument('-q', '--quiet', dest='loglevel', help='decrease output verbosity', action='store_const', const=logging.WARN)

	subparsers = parser.add_subparsers(title='commands (positional arguments)', help='Available commands', dest='command')

	scrape_parser = subparsers.add_parser('scrape', description='Scrape a website', help='Scrape a website')
	scrape_parser.add_argument('url', help='The url to the website you wish to scrape')
	scrape_parser.add_argument('target', help='The target that you want to scrape. Examples: h1, class name')
	scrape_parser.add_argument('target_type', choices=['tag', 'class', 'id'], help='The kind of target you wish to scrape')
	scrape_parser.add_argument('-t', '--tag', help='Scrape targets that uses this tag')
	scrape_parser.add_argument('-r', '--regex', dest='exp', help='Prettify the data using a regular expression')
	scrape_parser.add_argument('-u', '--user-agent', dest='agent', default='python_requests.cli-ws', help='Use this custom user agent')
	scrape_parser.add_argument('-f', '--filename', dest='name', default='data', help='The desired name for the file that will contain the data')
	scrape_parser.add_argument('-p', '--path', default='./', help='The complete path where you want the file that contains the data to be stored.')
	scrape_parser.add_argument('-ds', '--dont-save', help='Just output the data. Do not save it to a file', action='store_true')
	scrape_parser.add_argument('-kt', '--keep-tags', help='Keep the html tags when outputting data', action='store_true')

	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit(1)

	return parser.parse_args()
