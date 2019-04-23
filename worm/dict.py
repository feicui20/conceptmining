import pandas as pd

df = pd.read_excel('C:\\Users\\chenj\\Desktop\\mydict1.xlsx')
df = df[(df['isdict'] == 1) & (df['frequency'] > 18)]
print(df)
df2 = pd.DataFrame()
mydict = ''

for index, row in df.iterrows():
    df2 = df2.append({'word': row['word'],
                      'frequency': row['frequency'],
                      'isdict': row['isdict']}, ignore_index=True)
    mydict += row['word']
    mydict += '\n'
with open('real_dict.txt', 'w') as f:
    f.write(mydict)
df2.to_csv('real_dict.csv')
