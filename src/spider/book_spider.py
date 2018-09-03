# coding: utf-8

import requests
from codecs import open


base_url = 'https://www.555zw.com/book/4/4228/{}.html'
start_page = 2019643
end_page = 2020040

page_list = range(start_page, start_page + 3)
for page in page_list:
    url = base_url.format(page)
    rsp = requests.get(url, proxies={})
    if rsp.status_code == 200:
        print rsp.content

# with open('../../doc/novel.txt', 'w')



