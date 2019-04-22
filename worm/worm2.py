import requests
import http.cookiejar
import urllib

from bs4 import BeautifulSoup
s = requests.session()
url_1 = 'http://data.people.com.cn/rmrb/20190418/1?code=2'
url_2 = 'http://data.people.com.cn/sc/ss'
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    'Referer': 'http://data.people.com.cn/rmrb/20190418/1?code=2',
    'Cookie': 'td_cookie=18446744073097012688; JSESSIONID=045337BC36CEEBBCD19DAD9EAD06F1C7; targetEncodinghttp://127001=2; pageNo=1; _pk_id.2.6daf=9b1a63177d9c7635.1554870540.3.1555920258.1555920223.; pageSize=50; wdcid=5bd00245f9944250'
}

data = {
    'qs': '{"cIds":"23","cId":"23","cds":\
    [{"fld":"dataTime.start","cdr":"AND","hlt":"false","vlr":"AND","qtp":"DEF","val":"1978-01-01"},\
    {"fld":"dataTime.end","cdr":"AND","hlt":"false","vlr":"AND","qtp":"DEF","val":"2019-04-22"},\
    {"cdr":"AND","cds":[{"fld":"contentText","cdr":"AND","hlt":"true","vlr":"AND","qtp":"DEF","val":"三农"}]}],\
    "obs":[{"fld":"dataTime","drt":"DESC"}]}'
}


def get_cookie():
    cookie = http.cookiejar.MozillaCookieJar('cookie.txt')
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    request = urllib.request.Request(url=url_1, headers=headers1)
    opener.open(request)
    cookie.save()
    return cookie


def get_follow(url,data):
    ulist = []
    # data = urllib.parse.urlencode(data).encode('utf-8')
    r = requests.get(url, data=data, headers=headers2)
    print(r.text)


c = get_cookie()
# cookie_dict = {i.name: i.value for i in c}
get_follow(url_2, data)
# print(cookie_dict)
# headers2['Cookie'] = c
# get_follow(url_2)


# b_soup = BeautifulSoup(r.text, 'lxml')
# print(b_soup)
