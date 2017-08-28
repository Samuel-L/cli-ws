from setuptools import setup

setup(name='cliws',
    version='1.0',
    description='A command line web scraper',
    author='Samuel L',
    author_email='samuell.person@gmail.com',
    url='https://github.com/Samuel-L/web-scraper',
    packages=['web_scraper'],
    install_requires=[
        'beautifulsoup4==4.6.0',
        'click==6.7',
        'requests==2.18.4',
        'colorama==0.3.9'
    ],
    entry_points='''
        [console_scripts]
        cli-ws=web_scraper.cli:main
    ''',
)
