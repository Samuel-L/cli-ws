import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import click

from web_scraper.cli import scrapers


def invoke_scrape(ctx, task):
	ctx.invoke(scrapers.scrape, url=task['url'], target=task['target'], target_type=task['target_type'],
		no_prettify=task['no_prettify'], regex=task['regex'],
		filename=task['filename'], path=task['path'], dont_save=task['dont_save'],
		specific_tag=task['specific_tag']
	)


def echo_task(task):
	for column, value in task.items():
		click.echo(f'{column}: {value}')
