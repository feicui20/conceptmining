import pandas as pd


def get_real_dict_more_than_num(num1):
    df = pd.read_excel('C:\\Users\\chenj\\Desktop\\mydict1.xlsx')
    df = df[(df['isdict'] == 1) & (df['frequency'] > num1)]
    df2 = pd.DataFrame()
    my_dict = ''
    for index, row in df.iterrows():
        df2 = df2.append({'word': row['word'],
                          'frequency': row['frequency'],
                          'isdict': row['isdict']}, ignore_index=True)
        my_dict += row['word']
        my_dict += '\n'
    with open('real_dict_{}.txt'.format(num1), 'w') as f:
        f.write(my_dict)
    df2.to_csv('real_dict_{}.csv'.format(num1))


get_real_dict_more_than_num(100)

