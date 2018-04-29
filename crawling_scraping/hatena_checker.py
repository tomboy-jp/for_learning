import re
from pprint import pprint
from urllib.request import urlopen

def main(url):

    html = fetch(url)
    books = scrape(html)
    pprint(books)


def fetch(url):

    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj='utf-8')
    html = f.read().decode(encoding)

    return html


def scrape(html):

    books = []
    for partial_html in re.findall(r'<div class="entrylist-contents-main">.*?</div>\s*?</a>\s*?</div>\s*?</div>', html, re.DOTALL):

        try:
            title = re.search(r'data-gtm-click-label="entry-info-title">.*?</a>', partial_html).group()
            title = re.sub(r'<.*?>', '', title)
            title = re.sub(r'\u3000', ' ', title)
            title = re.sub(r'&amp;', '&', title)
            title = re.sub(r'data-gtm-click-label="entry-info-title">', '', title)

        except:
            title = ''

        try:
            users = re.search(r'data-gtm-click-label="entry-info-users"><span>.*?</span>', partial_html).group(0)
            users = re.sub(r'<.*?>', '', users)
            users = re.sub(r'data-gtm-click-label="entry-info-users">', '', users)

        except:
            users = 0

        books.append({'title': title, 'users': users})

    return books


if __name__ == '__main__':

     main("http://b.hatena.ne.jp/")
