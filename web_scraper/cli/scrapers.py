import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import click

from web_scraper.core import scrapers, html_fetchers, prettifiers, file_handlers


@click.command()
@click.argument('url')
@click.argument('target')
@click.argument('target_type', type=click.Choice(['tag', 'class', 'id']))
@click.option('--no-prettify', is_flag=True, help='Returns the raw data. No prettifier applied.')
@click.option('--regex', help='Apply this regular expression after the simple prettifer.')
@click.option('--specific-tag', help='Only scrape data that uses this tag.')
@click.option('--filename', default='data', help='Save the file with this name.')
@click.option('--path', default='./', help='Save the file to this path.')
@click.option('--dont-save', is_flag=True, help='Don\'t save the data to a file, only output it.')
def scrape(url, target, target_type, no_prettify, regex, filename, path, dont_save, specific_tag):
	"""Scrape the data from the given url

	URL         The url of the website you wish to scrape

	TARGET      The target that you wish to scrape from the website

	TARGET_TYPE The type of target you want to scrape (tag, class or id)
	"""
	html_document = str(html_fetchers.fetch_html_document(url))

	scraped_data = scrapers.scrape_target_elements(html_document,
		target=target,
		target_type=target_type,
		specific_tag=specific_tag
	)

	# when run_task invokes this function, no_prettify is a string, not a bool.
	if not no_prettify or no_prettify == 'False':
		scraped_data = prettifiers.simple_prettifier(scraped_data)
		if regex:
			scraped_data = prettifiers.regex_prettifier(scraped_data, regex)

	# when run_task invokes this function, dont_save is a string, not a bool.	
	if dont_save is True or dont_save == 'True':
		for data in scraped_data:
			click.echo(data)
		click.echo('\n')
	else:
		created_file_path = file_handlers.save_data_to_file(scraped_data,
			filename=filename,
			location=path
		)
		click.echo(f'Data saved to {created_file_path}\n')