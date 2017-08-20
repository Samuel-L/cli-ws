import requests


def return_html(url):
    try:
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            return res.text # html
        else:
            return res.status_code

    except requests.exceptions.ConnectionError as err:
        print() # CREATE BAD URL ERROR AND RETURN


if __name__ == '__main__':
    print(return_html('http://motherfuckingwebsite.com/doesnotexist'))