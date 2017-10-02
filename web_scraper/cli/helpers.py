import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from web_scraper.core import scrapers, html_fetchers, prettifiers, file_handlers

def scrape(url, target, target_type, specific_tag, regex, user_agent, filename,
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


def run_task(task):
	_scrape(task['url'], task['target'], task['target_type'], task['tag'],
		task['regex'], task['user_agent'], task['filename'], task['path'],
		task['dont_save'], task['keep_tags']
	)


def log_task(task):
	for column, value in task.items():
		logging.info(f'{column}: {value}')
	logging.info('\n')