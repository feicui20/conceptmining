import pandas as pd
import re
import jieba.analyse

df = pd.read_csv('1978to2019.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')


def connect(word_list, num):
    epoch = min(num+1, len(word_list))
    for i in range(epoch):
        for j in range(i+1, epoch):
            if word_list[i] in my_dict and word_list[j] in my_dict:
                graph_list.append([word_list[i], word_list[j]])
    if len(word_list) > num+1:
        for i in range(len(word_list)-num-1):
            if word_list[i+num] in my_dict:
                for j in range(i, i+num):
                    if word_list[j] in my_dict:
                        graph_list.append([word_list[j], word_list[i+num+1]])
            else:
                pass


global my_dict
my_dict = []
with open('real_dict.txt', 'r') as f:
    for i in f.readlines():
        my_dict.append("".join(i.split()))

for year in ['2008', '2018']:

    for i in range(len(df[year])):
        para = df[year].iloc[i]['para']
        para_n = re.findall(r"[\u4e00-\u9fff]+", para)
        para = "".join(para_n)
        word_list = jieba.cut(para)

        with open('{}.txt'.format(year), 'a') as f:
            f.write(" ".join(word_list))
            f.write('\n')


num = 10
for year in ['2008', '2018']:
    word_list = []
    graph_list = []
    with open('{}.txt'.format(year), 'r') as f:
        for line in f.readlines():
            word_list = line.split(" ")
            connect(word_list, 10)
    with open('graph{}.txt'.format(year), 'w') as f:
        for item in graph_list:
            f.write(" ".join(item))
            f.write('\n')






