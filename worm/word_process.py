import pandas as pd
import jieba
import jieba.analyse
import re

# jieba.load_userdict("mydict.txt")
stopwords_file = "C:\\Users\\chenj\\Desktop\\stopwords-master\\中文停用词表.txt"
jieba.analyse.set_stop_words('stop_large.txt')
df = pd.read_csv('1978to2019.csv')
df2 = pd.DataFrame()
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

stop_list = []
with open(stopwords_file, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        stop_list.append(line.strip())
# print(stop_list)
year_list = ["{}".format(i) for i in range(1978, 2020)]
para_list = ''
word_list = []
for year in year_list:
    try:
        for i in range(len(df[year])):
            para = df[year].iloc[i]['para']
            # para_n = re.sub(u"[\s\d\[\]\.\-%％+＋：．…。？！/《》“”‘’、,·，；（）【】—■]+", "", para)
            para_n = re.findall(r"[\u4e00-\u9fff]+", para)
            para_list += "".join(para_n)
    except:
        pass
#     for i in range(len(df[year])):
#         para = df[year].iloc[i]['para']
#         para_n = re.findall(r"[\u4e00-\u9fff]+", para)
#         para = "".join(para_n)
#         topKWords = jieba.analyse.extract_tags(para_n, topK=7)
#         word_list.append(topKWords)
# for item in word_list:
#     print('/'.join(item))
# print(para_list)
segments = dict()
print(len(para_list))
words = jieba.cut(para_list)
for word in words:
    if word in segments.keys():
        segments[word] += 1
    else:
        segments[word] = 1
stop = []

# for i in segments.keys():
#     if i in stop_list:
#         stop.append(i)
# # with open('stop.txt', 'w', encoding='utf-8') as f:
# #     for i in stop:
# #         f.write(str(i[0]) + '\t' + str(i[1]))
# #         f.write('\n')
#
# segments_sort = sorted(segments.items(), key=lambda item:item[1], reverse=True)
for i, j in segments.items():
    df2 = df2.append({'word': i, 'frequency': j, 'isdict': 0 if i in stop_list else 1}, ignore_index=True)
print(df2.head(10))
df2['frequency'] = df2['frequency'].astype("int")
df2['isdict'] = df2['isdict'].astype("int")
df2 = df2.sort_values(by=['frequency'], ascending=False)
df2.to_csv('mydict.csv')

# segments_fin = [i[0] for i in segments_sort if i[1]<7]
# segments_fin = list(set(segments_fin+stop))
# with open('stop_large.txt', 'w', encoding='utf-8') as f:
#     for i in segments_fin:
#         f.write(i)
#         f.write('\n')
# print(len(segments_fin))
# print(segments_fin)
# with open('C:\\Users\\chenj\\Desktop\\stopwords-master\\政治停用词表.txt', 'w', encoding='utf-8') as f:
#     for i in segments_sort:
#         f.write(i[0]+'\t'+str(i[1]))
#         f.write('\n')
# # print(df['1984'])
