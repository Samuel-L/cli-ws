from setuptools import setup

setup(name='cliws',
    version='1.0',
    description='A command line web scraper',
    license='MIT',
    author='Samuel L',
    author_email='samuell.person@gmail.com',
    url='https://github.com/Samuel-L/web-scraper',
    packages=['web_scraper.core', 'web_scraper.cli', 'web_scraper'],
    install_requires=[
        'beautifulsoup4==4.6.0',
        'requests==2.20.0',
    ],
    entry_points='''
        [console_scripts]
        cli-ws=web_scraper.__main__:main
    ''',
)
