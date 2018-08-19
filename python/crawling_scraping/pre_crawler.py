import requests
import lxml.html
import re
import time
from pymongo import MongoClient

def main():
    """
    クローラのメイン処理
    """

    client = MongoClient("localhost", 27017)
    collection = client.scraping.ebooks
    collection.create_index('key', unique=True)

    session = requests.Session()
    target = "https://gihyo.jp/dp"
    response = session.get(target)
    urls = scrape_list_page(response)

    for url in urls:

        key = extract_key(url)
        ebook =  collection.find_one({'key': key})

        if not ebook:
            time.sleep(1)

            try:
                response = session.get(url)
                ebook = scrape_detail_page(response)
                collection.insert_one(ebook)
                print(ebook)

            except:
                print("\nend")
                break

def scrape_list_page(response):
    """
    一覧ページのResponseから表歳ページのURLを抜き出すジェネレータ関数。
    """

    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)

    for a in root.cssselect('a[itemprop="url"]'):
        url = a.get("href")

        yield url

def scrape_detail_page(response):
    """
    詳細ページのResponoseから電子書籍の情報をdictで取得する。
    """

    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'key': extract_key(response.url),
        'title': root.cssselect('#bookTitle')[0].text_content(),
        'price': root.cssselect('.buy')[0].text,
        'content': [normalize_spaces(h3.text_content()) for h3 in root.cssselect('#content > h3')]
    }

    return ebook

def normalize_spaces(str):
    """
    連続する空白を一つのスペースに置き換え、前後の空白は削除した新しい文字列を取得する。
    """

    return re.sub(r'\s+', '', str).strip()

def extract_key(url):
    """
    URLからキー(URLの文末のISBN)を抜き出す。
    """
    
    m = re.search(r'/([^/]+)$', url)
    return m.group(1)

if __name__ == "__main__":

    main()
