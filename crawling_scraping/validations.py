import re
from voluptuous import Schema, Match

values = ['3000', '3,000', '-3000', '3,0,0,0']

for v in values:
    if not re.search(r'^[0-9,]+$', v):
        print("error")
    else:
        print("ok")


schema = Schema({
    'name': str,
    'price': Match(r'^[0-9,]+')
    }, required=True) # キー必須

schema({
    'name': 'ぶどう',
    'price': '3,000'
    })

schema({
    'name': None,
    'price': '3,000'
    }) # エラーになる
