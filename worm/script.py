# encoding=utf-8

import pandas as pd
import re
import jieba.analyse

# import the '1978to2019.csv' file
df = pd.read_csv('1978to2019.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')


# use connect function to link words

global my_dict
my_dict = []
with open('real_dict_100_1000.txt', 'r') as f:
    for i in f.readlines():
        my_dict.append("".join(i.split()))

year_list = ["{}".format(i) for i in range(2001, 2011)]
print(year_list)
for year in ['2001']:
    word_list = ""
    for i in range(len(df[year])):
        para = df[year].iloc[i]['para']
        if not pd.isnull(para):
            para_n = re.findall(r"[\u4e00-\u9fff]+", para)
            para = "".join(para_n)
            para = "".join(para.split())
            para = jieba.cut(para)
            para = [item for item in para if item in my_dict]
            print(para)



