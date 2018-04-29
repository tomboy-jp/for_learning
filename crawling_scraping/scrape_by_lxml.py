import lxml.html
import requests
from pprint import pprint

html = requests.get("https://www.yahoo.co.jp/").text
tree = lxml.html.fromstring(html)

list = [a.get('href') for a in tree.cssselect('a')]
pprint(list)
