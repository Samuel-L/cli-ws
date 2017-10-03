import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from web_scraper.cli import scraper


def run_task(task):
	scraper.scrape(task['url'], task['target'], task['target_type'], task['tag'],
		task['regex'], task['user_agent'], task['filename'], task['path'],
		task['dont_save'], task['keep_tags']
	)


def log_task(task):
	for column, value in task.items():
		logging.info(f'{column}: {value}')
	logging.info('\n')
