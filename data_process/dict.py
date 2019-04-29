# coding:utf-8

import pandas as pd
import sys
import argparse


def main(args):
    input_file = args.input_file
    output_dir = args.output_dir
    begin = args.begin
    get_real_dict_more_than_num(input_file, output_dir, begin)


def get_real_dict_more_than_num(input_file, output_dir, begin):
    df = pd.read_excel(input_file)
    df = df[(df['isdict'] == 1) & (df['frequency'] > begin)]
    df2 = pd.DataFrame()
    my_dict = ''
    for index, row in df.iterrows():
        df2 = df2.append({'word': row['word'],
                          'frequency': row['frequency'],
                          'isdict': row['isdict']}, ignore_index=True)
        my_dict += row['word']
        my_dict += '\n'
    with open(output_dir + '\\real_dict_{}.txt'.format(begin), 'w', encoding='utf-8') as f:
        f.write(my_dict)
    df2.to_csv(output_dir + '\\real_dict_{}.csv'.format(begin))


def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--input_file', type=str, default='C:\\Users\\chenj\\Desktop\\mydict1.xlsx',
                        help='Dict file.')
    parser.add_argument('--output_dir', type=str, default='..\\data\\usage',
                        help='Real dict directory.')
    parser.add_argument('--begin', type=int, default=100,
                        help='The number stop words begin from.')

    return parser.parse_args(argv)


if __name__ == "__main__":
    main(parse_arguments(sys.argv[1:]))
