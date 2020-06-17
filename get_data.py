import requests
import re
from bs4 import BeautifulSoup

query_search = 'https://zenodo.org/record/3884124#.XugKgC2w3OS'
page = requests.get(query_search)
page_parsed = BeautifulSoup(page.text, 'html.parser')

links_list = page_parsed.find_all('link')[8:]
links_list_nice = [re.findall(r'href="(.+?)" rel', url.prettify())[0] for url in links_list]

for link in links_list_nice:
    r = requests.get(link)
    print('json_covid/'+link[-26:])
    with open('json_covid/'+link[-26:], 'wb') as f:
        f.write(r.content)