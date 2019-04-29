# encoding=utf-8

import pandas as pd
import re
import jieba.analyse
import argparse
import sys


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


def main(args):

    # import the '1978to2019.csv' file
    csv_file = args.csv_file
    dict_file = args.dict_file
    output_dir = args.output_dir
    begin = args.begin
    end = args.end
    num = args.num
    global my_dict
    global graph_list
    year_list = ["{}".format(i) for i in range(begin, end+1)]
    df = pd.read_csv(csv_file)
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')

    with open(dict_file, 'r', encoding='utf-8') as f:
        my_dict = []
        for i in f.readlines():
            my_dict.append("".join(i.split()))

    for year in year_list:
        word_list = ""
        for i in range(len(df[year])):
            para = df[year].iloc[i]['para']
            if not pd.isnull(para):
                para_n = re.findall(r"[\u4e00-\u9fff]+", para)
                para = "".join(para_n)
                para = "".join(para.split())
                word_list += " ".join(jieba.cut(para))+'\n'

        with open(output_dir+'\\{}.txt'.format(year), 'w', encoding='utf-8') as f:
            f.write(word_list)

    for year in year_list:
        graph_list = []
        with open(output_dir+'\\{}.txt'.format(year), 'r', encoding='utf-8') as f:
            for line in f.readlines():
                word_list = line.split()
                connect(word_list, num)
        with open(output_dir+'\\graph{}.txt'.format(year), 'w', encoding='utf-8') as f:
            for item in graph_list:
                f.write(" ".join(item)+'\n')


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--csv_file', type=str, default='..\\data\\raw\\1978to2019.csv',
                        help='Csv file.')
    parser.add_argument('--dict_file', type=str, default='..\\data\\usage\\real_dict_100.txt',
                        help='Dict file.')
    parser.add_argument('--output_dir', type=str, default='..\\data\\graph',
                        help='Output directory.')
    parser.add_argument('--begin', type=int, default=2001,
                        help='The year begin from.')
    parser.add_argument('--end', type=int, default=2018,
                        help='The year end from.')
    parser.add_argument('--num', type=int, default=2,
                        help='Number that we concerned.')

    return parser.parse_args(argv)


if __name__ == "__main__":
    main(parse_arguments(sys.argv[1:]))
