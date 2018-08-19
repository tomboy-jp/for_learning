import requests
from pprint import pprint

r = requests.get("http://weather.livedoor.com/forecast/webservice/json/v1?city=130010")
pprint(r.json())
