import pandas as pd
import numpy as np

df_grade = pd.DataFrame({'Alice': [1,2,3,4,5], 
                         'Chuck': np.random.random(5),
                         'Bob': np.random.random(5)},
                        index = ['Jan', 'Feb', 'Mar', 'Apr', 'May'])

print(df_grade)
print(type(df_grade['Alice']))

# Indexing
print(df_grade['Alice'])
print(df_grade['Alice'].iloc[1])
print(df_grade['Alice'].loc['Jan'])

# Iterating over a dataframe

for key, value in df_grade['Alice'].iteritems():
    print('Key {} and value {}'. format(key,value))
# Dataframes supports iteration over the index

for index, rows in df_grade.iterrows():
    print('Index = {} and Rows = {}'.format(index, rows['Alice']))

# DATAFRAME MANIPULATION
# Fetching a series column in a dataframe with a list gives a dataframe with that series
print(df_grade[['Alice']])

# Extracting a column as a new dataframe
df_col = df_grade[['Alice']]
print(df_col,'\n', type(df_col) )

# Extracting a row as a new dataframe
df_row = df_grade.loc['Jan':'Jan']
print(df_row, '\n', type(df_row))

# Slicing along rows works as just as with series
print(df_grade.loc['Jan': 'Mar', 'Alice'])
# Slicing along columns
print(df_grade.loc[:, 'Alice' : 'Bob'])
