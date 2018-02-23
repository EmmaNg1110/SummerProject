#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:05:52 2018

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

spei_site = spei.sel(lat=-31.6779,lon=115.6961,method='nearest')

#Start and end day of interested period, which is the same as the anomoly period

start_date='1992-01'

end_date='2016-01'

spei_site = spei_site.sel(time=slice(start_date,end_date))

spei_site.plot()


#Read the file
file_new = '/home/emma/Downloads/qrk11.csv'

# read file using pandas (pd)

df = pd.read_csv(file_new, sep=',', error_bad_lines=False, index_col=False)

df['date'] = pd.to_datetime(df['date'])


df2 = read_csv('/home/emma/Downloads/qrk92.csv')

df2['date'] = pd.to_datetime(df2['date'])


frames = [df2[['date', 'PM2.5']], df[['date', 'PM2.5']]]

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
    rolling = new1[['PM2.5']][new1.mon==i].rolling(window = 7, center=True)

    rolling_mean = rolling.mean()
    
    
    anomoly = (new1['PM2.5'][new1.mon==i]) - rolling_mean['PM2.5']


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
plt.title('Caversham_PM2.5')
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
