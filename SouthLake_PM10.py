#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:28:45 2018

@author: emma
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
from matplotlib import pyplot
from scipy import stats

#Opening an NETCDF File
dataset = xr.open_dataset('/home/emma/Downloads/spei01.nc')

#To convert the DataFrame to any other convenient representation
#df = dataset.to_dataframe()


#Plotting Bargo with a latitude of -34.3075 and a longtitude of 150.58
spei = dataset.spei

spei_site = spei.sel(lat=-32.1106,lon=115.8348,method='nearest')


#Start and end day of interested period, which is the same as the anomoly period

start_date='2000-01'

end_date='2016-01'

spei_site = spei_site.sel(time=slice(start_date,end_date))

spei_site.plot()


#Read the file
file_new = '/home/emma/Downloads/slk11.csv'

# read file using pandas (pd)

df = pd.read_csv(file_new, sep=',', error_bad_lines=False, index_col=False)

df['date'] = pd.to_datetime(df['date'])


df2 = read_csv('/home/emma/Downloads/slk00.csv')

df2['date'] = pd.to_datetime(df2['date'])


frames = [df2[['date', 'PM10']], df[['date', 'PM10']]]

data = pd.concat(frames)

data['date'] = pd.to_datetime(data['date'])

data['mon'] = data['date'].dt.month

data = data.set_index('date')

data_mm = data.resample('M').mean()



#But our data are monthly means, so they are related not to some particular 
#point in time, but rather to the time interval, or time span. 
#We can convert time stamps in our Series to time periods, and then combine them.

new1 = data_mm.to_period(freq='M')


for i in range (1,13): 
    rolling = new1[['PM10']][new1.mon==i].rolling(window = 7, center=True)

    rolling_mean = rolling.mean()
    
    
    anomoly = (new1['PM10'][new1.mon==i]) - rolling_mean['PM10']


#Putting all months together
    if i == 1:
        al1 = anomoly
        
    else:
        temp = anomoly
        al1 = pd.concat([al1, temp])


#sorting the entire dataframe according to index

al1=al1.sort_index()

al1.plot(label='Anomoly')

plt.grid(True)
plt.legend(loc='best')
plt.title('SouthLake_PM10')
plt.show()



mask = ~np.isnan(spei_site) & ~np.isnan(al1)

RegressResult = stats.linregress(spei_site[mask], al1[mask])

slope, intercept, r_value, p_value, std_err = stats.linregress(spei_site[mask], al1[mask])

print (RegressResult)


#Plot the data along with the fitted line
plt.plot(spei_site, al1, 'o', label='Original Data')
plt.plot(spei_site, intercept + slope*spei_site, 'r', label='Fitted Line')
plt.xlabel('SPEI')
plt.ylabel('Anomoly')
plt.legend()
plt.show()

data1 = spei_site.to_dataframe()

data1 = data1.reset_index()

al1 = al1.reset_index()

result1 = pd.concat([data1['spei'], al1['PM10']], axis=1)

N = len(data_mm['PM10'][~np.isnan(data_mm['PM10'])])

drought1 = result1[['spei', 'PM10']][data1.spei < -1.3]

print("Drought months: ", (len(drought1['PM10'][~np.isnan(drought1['PM10'])]))*100/N)

wet1 = result1[['spei', 'PM10']][data1.spei > -1.3]

print("Wet months: ", (len(wet1['PM10'][~np.isnan(wet1['PM10'])]))*100/N)
