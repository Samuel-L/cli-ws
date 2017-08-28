import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import click

from web_scraper import core

@click.command()
@click.argument('url')
@click.argument('target')
@click.argument('target_type')
@click.option('--location', default='./')
@click.option('--filename', default='data')
@click.option('--no-prettify', default=False, is_flag=True)
@click.option('--dont-save', default=False, is_flag=True)
def main(url, target, target_type, location, filename, dont_save, no_prettify):
    """Entry Point"""
    html_document = str(core.fetch_html_document(url))

    scraped_data = core.scrape_target_elements(
        html_document,
        target=target,
        target_type=target_type
    )

    if not no_prettify:
        scraped_data = core.prettify_scraped_data(scraped_data)

    if dont_save:
        for item in scraped_data:
            click.echo(item)
    else:
        created_file_location = core.save_data_to_file(
            scraped_data,
            filename=filename,
            location=location
        )
        click.echo(f'Data saved to {created_file_location}!')


if __name__ == '__main__':
    main()