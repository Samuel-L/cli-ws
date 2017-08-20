def fetch_local_html():
    with open('./tests/motherfuckingwebsite.html', 'r') as file:
        return file.read()
