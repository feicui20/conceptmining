import pandas as pd
import re
import jieba.analyse

df = pd.read_csv('1978to2019.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')


for year in ['2008', '2018']:
    word_list = []
    for i in range(len(df[year])):
        para = df[year].iloc[i]['para']
        para_n = re.findall(r"[\u4e00-\u9fff]+", para)
        para = "".join(para_n)
        topKWords = jieba.analyse.extract_tags(para_n, topK=7)
        word_list.append(topKWords)
    with open('')


