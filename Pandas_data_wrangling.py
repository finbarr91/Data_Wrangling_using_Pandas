import pandas as pd
import numpy as np
from pandas_datareader import data as pd_data
import matplotlib.pyplot as plt
from collections import OrderedDict

# Reading data from the web
# start = pd.Timestamp('2010-1-1')
# end = pd.Timestamp('2014-12-31')
# data= pd_data.DataReader('GOOG','google',start,end)
#
# The above code is how i generated the data file read above

data = pd.read_csv('https://raw.githubusercontent.com/finbarr91/Learning-Pandas-Second-Edition/master/data/goog.csv', index_col = 'Date', parse_dates=True)
print(data.head(20))
print(type(data))
print(data.info())

print(data['Open'])

# Inspecting the first five rows of the Open column using the integer indexing
print(data['Open'].iloc[0:5])

# Inspecting the first five rows of the Open column using the date indexing
print(data.loc['2017-01-04':'2017-01-08', 'Open'])

# Data Filtering
data_up = data[data['Close']>data['Open']]
print(data_up.head)

# Filtering our missing data.
data_filtered = data[pd.isnull(data['Volume']==False)]
print(data_filtered.head())

# Data Statistics
print(data.describe())

# Data Computation
# One simple example motivated by finance is to compute the volatility -- the rolling standard deviation of the log return over the business days of the year
# First we use the pandas method.pct_change( to compute the return pre day based on percent change
# Next we use the numpy to compute the log of the return
# Finally we use pandas method.rolling_std() to compute the volatility

# Compute the return from daily percent change
# Append a new column
data['Return'] = data['Close'].pct_change()
print(data['Return'].iloc[0:5])

# Compute the log of the Return using numpy
# Append another new column
data['LogReturn']= np.log(1+data['Return'])
print(data['LogReturn'].iloc[0:5])

# Compute volatility as rolling standard deviation of the log() of the returns.
# Append yet another new column
window_size = 252
data['Volatility'] = data['LogReturn'].rolling(window_size, min_periods=1).std()*np.sqrt(window_size)
print(data['Volatility'].iloc[window_size-5:window_size+5])
print('Volatility Column:\n', data['Volatility'].values)

# Plotting Close and Volatility
data[['Close', 'Volatility']].plot(subplots = True, figsize=(16,6))
plt.show()


# How to create a pandas series from a list
my_list = [2,3,4,5]
print(pd.Series(my_list))

# How to create a pandas from a dictionary
my_dict = {'b':2000, 'a':1000, 'd':6677, 'c':6, 'z':1, 'e':0}
print(my_dict)
print(pd.Series(my_dict))

# Selecting Series from Ordered dictionary to preserve the order of indices
od = OrderedDict([('b', 100), ('a', 30), ('f', 65), ('d', 120)])
print(od)
print(pd.Series(od))

# Creating a Series from Numpy array

arr = np.arange(1,6)*10.0
print(arr)
arr1 = pd.Series(arr)
print(arr1)
print(type(arr))
print(type(arr1))
