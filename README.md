# CLI-WS
Cli-ws is a simple web scraper made for the command line.

![Usage image](https://i.imgur.com/L8sxG6S.gif)

Prerequisite
------------
* Python 3.6

Installation
------------
1. Download (or clone) this repository
2. Extract the cli-ws folder
3. Navigate to the extracted folder
5. Run `$ python setup.py install`

Usage
------------
```
$ cli-ws --help
usage: cli-ws [-h] [-v | -q]
              {scrape,create_task,run_task,show_task,remove_task} ...

A web scraper for the command line

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -q, --quiet           decrease output verbosity

commands (positional arguments):
  {scrape,create_task,run_task,show_task,remove_task}
                        Available commands
    scrape              Scrape a website
    create_task         Create a task
    run_task            Run a task
    show_task           Show task(s)
    remove_task         Remove a task
```

Tests
------------
1. Install [nose](http://nose.readthedocs.io/en/latest/)
2. Navigate to the `cli-ws` folder
3. Run `nosetests tests/`

## License

[MIT](LICENSE)
