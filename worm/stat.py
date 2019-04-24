# encoding=utf-8

import pandas as pd
import matplotlib.pyplot as plt


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


plot_dict_with_sw()
plot_dict_without_sw()