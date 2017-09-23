import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import click

from web_scraper.cli import tasks, scrapers


@click.group()
def cli():
	pass


if __name__ == '__main__':
	cli.add_command(scrapers.scrape)
	cli.add_command(tasks.create_task)
	cli.add_command(tasks.run_task)
	cli.add_command(tasks.remove_task)
	cli.add_command(tasks.show_task)
	cli()
