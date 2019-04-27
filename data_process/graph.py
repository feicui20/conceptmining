# encoding=utf-8

import pandas as pd
import re
import jieba.analyse

# import the '1978to2019.csv' file
df = pd.read_csv('1978to2019.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')


# use connect function to link words
def connect(word_list, num):
    epoch = min(num+1, len(word_list))
    for i in range(epoch):
        for j in range(i+1, epoch):
            if word_list[i] in my_dict and word_list[j] in my_dict:
                graph_list.append([word_list[i], word_list[j]])
    if len(word_list) > num+1:
        for i in range(len(word_list)-num-1):
            if word_list[i+num+1] in my_dict:
                for j in range(i+1, i+num+1):
                    if word_list[j] in my_dict:
                        graph_list.append([word_list[j], word_list[i+num+1]])
            else:
                pass


global my_dict
my_dict = []
with open('real_dict_100_1000.txt', 'r') as f:
    for i in f.readlines():
        my_dict.append("".join(i.split()))

year_list = ["{}".format(i) for i in range(2001, 2011)]
print(year_list)
for year in year_list:
    word_list = ""
    for i in range(len(df[year])):
        para = df[year].iloc[i]['para']
        if not pd.isnull(para):
            para_n = re.findall(r"[\u4e00-\u9fff]+", para)
            para = "".join(para_n)
            para = "".join(para.split())
            word_list += " ".join(jieba.cut(para))
            word_list += '\n'

    with open('{}.txt'.format(year), 'w', encoding='utf-8') as f:
        f.write(word_list)


num = 2
for year in year_list:
    word_list = []
    graph_list = []
    with open('{}.txt'.format(year), 'r', encoding='utf-8') as f:
        for line in f.readlines():
            word_list = line.split()
            connect(word_list, num)
    with open('graph{}.txt'.format(year), 'w', encoding='utf-8') as f:
        for item in graph_list:
            f.write(" ".join(item))
            f.write('\n')






