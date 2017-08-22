def fetch_local_html(html):
    with open(f'./tests/html_for_tests/{html}.html', 'r') as file:
        return file.read()
