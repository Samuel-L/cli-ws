import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import click

from web_scraper import file_handlers, html_fetchers, proxy_pinger
from web_scraper import scrapers, prettifiers


@click.group()
def cli():
    pass


@click.command()
@click.option('--specific-tag', default='', help='Only scrape target if it has '
             'this tag.')
@click.option('--no-prettify', default=False, is_flag=True,  help='Don\'t prettify the '
              'scraped data.')
@click.option('--filename', default='data', help='Custom filename for the data '
              'file')
@click.option('--path', default='./', help='Custom file path for the data '
              'file.')
@click.option('--dont-save', default=False, is_flag=True,  help='Don\'t save the data to '
              'file. Just output it.')
@click.option('--regex-prettifier', default='', help='Prettify the data using '
              'regex. Applied after the simple prittifer')
@click.argument('url')
@click.argument('target')
@click.argument('target_type', type=click.Choice(['tag', 'class', 'id']))
def scrape(url, target, target_type, specific_tag, no_prettify, filename, path,
          dont_save, regex_prettifier):
    html_document = str(html_fetchers.fetch_html_document(url))

    scraped_data = scrapers.scrape_target_elements(html_document,
                                                   target=target,
                                                   target_type=target_type,
                                                   specific_tag=specific_tag)
    if not no_prettify:
        scraped_data = prettifiers.simple_prettifier(scraped_data)
        if regex_prettifier:
            scraped_data = prettifiers.regex_prettifier(scraped_data,
                                                        regex_prettifier)

    if dont_save:
        for data in scraped_data:
            click.echo(data)
    else:
        created_file_path = file_handlers.save_data_to_file(scraped_data,
                                                            filename=filename,
                                                            location=path)
        click.echo(f'Data saved to {created_file_path}!')


if __name__ == '__main__':
    cli.add_command(scrape)
    cli()

