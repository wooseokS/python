import pandas as pd
import numpy as np
# ~~ data read ~~
CCTV_Seoul = pd.read_csv('pandas/01. CCTV_in_Seoul.csv', encoding='utf-8')
CCTV_Seoul.rename(columns = {CCTV_Seoul.columns[0] : '구별'}, inplace = True)
pop_Seoul = pd.read_excel('pandas/01. population_in_Seoul.xls', header=2, usecols= 'B, D, G, J, N')
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별',
                        pop_Seoul.columns[1] : '인구수',
                        pop_Seoul.columns[2] : '한국인',
                        pop_Seoul.columns[3] : '외국인',
                        pop_Seoul.columns[4] : '고령자'}, inplace=True)

s = pd.Series([1,3,5,np.nan,6,8])
# print(s)

# ~~ data frame processing ~~

dates = pd.date_range('20130101', periods = 6)
# print(dates)

df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = ['A', 'B', 'C', 'D'])
# print(df.describe())
# df = df.sort_values(by='B', ascending=False)
# print(df[df > 0])

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
# print(df2[df2['E'].isin(['two', 'four'])])

# print(df)
# print(df.apply(np.cumsum))
# print(df.apply(lambda x: x.std()))
# print(CCTV_Seoul.sort_values(by='소계', ascending=False).head(5))

# ~~ Seoul CCTV data processing ~~
CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전'] * 100
# print(CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(5))


# ~~ Seoul population data processing ~~
pop_Seoul.drop([0], inplace=True)
print(pop_Seoul.head())

print(pop_Seoul['구별'].unique())

print(pop_Seoul[pop_Seoul['구별'].isnull()])
pop_Seoul.drop([26], inplace=True)
print(pop_Seoul.head())
pop_Seoul['외국인비율'] = pop_Seoul['외국인']/pop_Seoul['인구수'] * 100
pop_Seoul['고령자비율'] = pop_Seoul['고령자']/pop_Seoul['인구수'] * 100
print(pop_Seoul.head())

print(pop_Seoul.sort_values(by='인구수', ascending=False).head())
print(pop_Seoul.sort_values(by='외국인', ascending=False).head())
print(pop_Seoul.sort_values(by='외국인비율', ascending=False).head())

# ~~ dataframe 병합 ~~
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index = [0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index = [4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index = [8, 9, 10, 11])
result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])
print(result)
df4 = pd.DataFrame({'B' : ['B2', 'B3', 'B6', 'B7'],
                    'D' : ['D2', 'D3', 'D6', 'D7'],
                    'F' : ['F2', 'F3', 'F6', 'F7']},
                    index = [2, 3, 6, 7])
result = pd.concat([df1, df4], axis = 1)
result = pd.concat([df1, df4], axis = 1, join = 'inner')
result = pd.concat([df1, df4], axis = 1).reindex(df1.index)

result = pd.concat([df1, df4], ignore_index = True)
print(result)

# ~~ key merge ~~
'''
left = pd.DataFrame({'key': ['K0', 'K4', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key' : ['K0', 'K1', 'K2', 'K3'],
                        'C' : ['C0', 'C1', 'C2', 'C3']})
                        '''