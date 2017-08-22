def fetch_local_html(html):
    with open(f'./tests/{html}.html', 'r') as file:
        return file.read()
