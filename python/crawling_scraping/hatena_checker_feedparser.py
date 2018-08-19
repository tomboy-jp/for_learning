import feedparser

d = feedparser.parse('http://b.hatena.ne.jp/hotentry/it.rss')
type(d)
d.version
d.feed
d.feed.title
d['feed']['title']
d.feed.link
d.feed.description
len(d.entries)
d.entries[0].title
d.entries[0].link
d.entries[0].description
d.entries[0].updated
d.entries[0].updated_parsed

for entry in d.entries:
    print(entry.link, entry.title)
