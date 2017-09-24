import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def return_html_document():
	"""Return the 'github-python-trending' html document"""
	with open('tests/test_files/html-document.html', 'r') as html_file:
		html_document = html_file.read()
	return html_document
