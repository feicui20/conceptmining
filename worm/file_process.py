#coding:utf-8

import glob
from bs4 import BeautifulSoup
import pandas as pd
import re

pd.set_option('display.max_columns', None)
df = pd.DataFrame()
pattern_author = re.compile(u"^作者：(.+)&")
pattern_date = re.compile(u'时间：(\d+-\d+-\d+)')
for name in glob.glob('C:\\Users\\chenj\\Desktop\\peopledata*\\index.html'):
    with open(name, 'r', encoding='utf-8') as f:
        bsoup = BeautifulSoup(f, 'lxml')
    for item in bsoup.find_all('div', id='jqprint'):
        title_div = item.find('div', class_='title')
        title_first = title_div.h2.text
        if title_div.h3:
            title_second = title_div.h3.text
        else:
            title_second = ''
        author_and_date = title_div.p
        if author_and_date:
            author = re.findall(pattern_author, author_and_date.text)[0]
            date = re.findall(pattern_date, author_and_date.text)[0]
        else:
            author = ''
            date = ''
            if re.findall(pattern_date, title_div.text):
                date = re.findall(pattern_date, title_div.text)[0]
        article = item.find('div', id='detail-p').find_all('p')
        para = ''
        for a in article:
            para += a.text

        df = df.append({'title_first': title_first,
                        'title_second': title_second,
                        'author': author,
                        'date': date,
                        'para': para},
                       ignore_index=True)

        pass
df = df.sort_values(by=['date'])
df['date'] = pd.to_datetime(df['date'])
print(df.info())
df.to_csv('1978to2019.csv')
