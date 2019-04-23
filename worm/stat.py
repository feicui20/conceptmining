# encoding=utf-8
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mydict.csv')

l = list(df['frequency'])
plt.hist(l, bins=500, range=(18, 5500), log=True)
plt.title('Frequency-Amount(Log) relationship with stop word')
plt.xlabel('Frequency')
plt.ylabel('Amount(Log)')
plt.savefig('FARSW.png', dpi=300)
plt.show()

