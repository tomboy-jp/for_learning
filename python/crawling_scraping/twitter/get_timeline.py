import os
from requests_oauthlib import OAuth1Session

CONSUMER_KEY = os.environ['TWTTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

twitter = OAuth1Session(
    CONSUMER_KEY,
    client_secret=CONSUMER_SECRET,
    resource_owner_key=ACCESS_TOKEN,
    resource_owner_secret=ACCESS_TOKEN_SECRET
    )

response = twitter.get('https://api.twitter.com/1.1/statuses/home_timeline.json')

for status in response.json():
    print('@' + status['user']['screen_name'], status['text'])
