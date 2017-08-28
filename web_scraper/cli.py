import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import click

from web_scraper import core

def _verbose_echo(echo_string, verbose):
    if verbose:
        click.secho(echo_string, fg='green')


@click.command()
@click.argument('url')
@click.argument('target')
@click.argument('target_type')
@click.option('--location', default='./', help='The location that you want the data file to be saved to')
@click.option('--filename', default='data', help='The filename you want the data file to have')
@click.option('--no-prettify', default=False, is_flag=True, help="Use this flag if you don't want prettified data")
@click.option('--dont-save', default=False, is_flag=True, help="This won't save the data to a file, just output it")
@click.option('--verbose', default=False, is_flag=True, help="Show verbose messages")
def main(url, target, target_type, location, filename, no_prettify, dont_save, verbose):
    """A command line web scraper


        Arguments:

            url: the website you want to scrape for data

            target: tag, class or id that you want to scrape

            target_type: the type of target you want to scrape


        Examples:

            cli-ws example.com p tag

            cli-ws example.com class_name class

            cli-ws example.com id_name id
    """
    html_document = str(core.fetch_html_document(url))
    _verbose_echo(f'Html document fetched from {url}.', verbose)
    
    scraped_data = core.scrape_target_elements(
        html_document,
        target=target,
        target_type=target_type
    )
    _verbose_echo(f'Scraped all "{target}" targets with type "{target_type}" from the document.', verbose)

    if not no_prettify:
        scraped_data = core.prettify_scraped_data(scraped_data)
        _verbose_echo(f'The scraped data has been prettified', verbose)

    if dont_save:
        for item in scraped_data:
            click.echo(item)
    else:
        created_file_location = core.save_data_to_file(
            scraped_data,
            filename=filename,
            location=location
        )
        click.secho(f'Data saved to {created_file_location}!', fg='green')


if __name__ == '__main__':
    main()