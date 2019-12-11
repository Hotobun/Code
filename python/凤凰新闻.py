import requests
from lxml import etree

url = 'http://www.ifeng.com/'
head = {
        "user-agent":'mozilla/5.0',
        'referer':"http://tech.ifeng.com"
	}
r = requests.get(url, headers = head)
r.encoding = 'utf-8'
html = etree.HTML(r.text)
ul = html.xpath('//ul[@class="news_list-3wjAJJJM"]')
for li in ul:
    for i in li:
        text = i.xpath("./a/text()")
        if len(text):
            print(text[0])

