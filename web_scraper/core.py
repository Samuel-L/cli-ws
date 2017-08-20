import requests
from requests.exceptions import ConnectionError, MissingSchema

def return_html(url):
    try:
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            return res.text # html
        else:
            return res.status_code

    except (ConnectionError, MissingSchema) as err:
        if type(err) == MissingSchema:
            return f'INVALID URL: {url} misses schema! Did you mean: http://{url}'
        elif type(err) == ConnectionError:
            return f'INVALID URL: {url} does not exist!'


if __name__ == '__main__':
    pass