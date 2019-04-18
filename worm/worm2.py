import requests
import urllib.request
from bs4 import BeautifulSoup
s = requests.session()
url = 'http://data.people.com.cn/rmrb/20190418/1?code=2'
url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
}
r = s.get(url)
b_soup = BeautifulSoup(r)
print(b_soup)
