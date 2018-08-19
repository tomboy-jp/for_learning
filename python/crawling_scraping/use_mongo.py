import lxml.html
from pymongo import MongoClient
import requests

data = requests.get("https://gihyo.jp/dp")
html = lxml.html.fromstring(data.content)
html

client = MongoClient('localhost', 27017)
db = client.scraping
collection = db.links

collection

collection.delete_many({})

for a in html.cssselect('a'):
    collection.insert_one({'url': a.get('href'), 'title': a.text,})

for link in collection.find().sort('_id'):
    print(link['_id'], link['url'], link['title'])
