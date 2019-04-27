# encoding=utf-8

import pandas as pd
import matplotlib.pyplot as plt
import re


def plot_dict_with_sw():
    df = pd.read_csv('mydict.csv')
    frequency = list(df['frequency'])
    plt.hist(frequency, bins=500, range=(18, 5500), log=True)
    plt.title('Frequency-Amount(Log) relationship with stop word')
    plt.xlabel('Frequency')
    plt.ylabel('Amount(Log)')
    plt.savefig('FARSW.png', dpi=300)
    plt.show()


def plot_dict_without_sw():
    df = pd.read_csv('real_dict.csv')
    frequency = list(df['frequency'])
    plt.hist(frequency, bins=500, range=(18, 5500), log=True)
    plt.title('Frequency-Amount(Log) relationship without stop word')
    plt.xlabel('Frequency')
    plt.ylabel('Amount(Log)')
    plt.savefig('FARNSW.png', dpi=300)
    plt.show()


def main():
    plot_dict_with_sw()
    plot_dict_without_sw()


def plot_dict_without_sw_v2(filename, bin, save):
    num_pair = re.findall(r'\d+', filename)
    num1 = int(num_pair[0])
    num2 = int(num_pair[1])
    df = pd.read_csv(filename)
    frequency = list(df['frequency'])
    plt.hist(frequency, bins=bin, range=(num1, num2), log=True)
    plt.title('Frequency-Amount(Log) relationship without stop word from {} to {}'.format(num1, num2))
    plt.xlabel('Frequency')
    plt.ylabel('Amount(Log)')
    if save:
        plt.savefig('FARNSW_{}_{}.png'.format(num1, num2), dpi=300)
    plt.show()



plot_dict_without_sw_v2('real_dict_100_1000.csv', 20, 1)
