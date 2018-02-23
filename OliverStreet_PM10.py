#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:05:17 2018

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


#Plotting LeFevre with a latitude of -34.80 and a longtitude of 138.49
spei = dataset.spei

spei_site = spei.sel(lat=-33.1708,lon=138.0089,method='nearest')

#Start and end day of interested period, which is the same as the anomoly period

start_date='2001-01'

end_date='2018-01'

spei_site = spei_site.sel(time=slice(start_date,end_date))

spei_site.plot()


#Read the file
df = read_csv('/home/emma/Documents/SA/Oliver Street_PM10_2005-2017.csv')


df['Date'] = pd.to_datetime(df['Date'])

df['mon'] = df['Date'].dt.month

df = df.set_index('Date')


new = df['PM10 '].resample('M').mean()

new = new.to_period(freq='M')

new = new.to_frame()

new = new.reset_index()

new['mon'] = new['Date'].dt.month

new = new.set_index('Date')


for i in range (1,13): 
    rolling = new[['PM10 ']][new.mon==i].rolling(window = 5, center=True)

    rolling_mean = rolling.mean()
    
    
    anomoly = (new['PM10 '][new.mon==i]) - rolling_mean['PM10 ']


#Putting all months together
    if i == 1:
        al1 = anomoly
        
    else:
        temp = anomoly
        al1 = pd.concat([al1, temp])


#sorting the entire dataframe according to index

al1=al1.sort_index()

al1.plot(label='Anomoly')

pyplot.grid(True)
pyplot.legend(loc='best')
pyplot.title('LeFevre_PM10')
pyplot.show()



mask = ~np.isnan(spei_site) & ~np.isnan(al1)

RegressResult = stats.linregress(spei_site[mask], al1[mask])

slope, intercept, r_value, p_value, std_err = stats.linregress(spei_site[mask], al1[mask])

N = len(spei_site[mask])

print (RegressResult)
print (N)


#Plot the data along with the fitted line
plt.plot(al1,spei_site, 'o', label='Original Data')
plt.plot(al1, intercept + slope*al1, 'r', label='Fitted Line')
plt.xlabel('Anomoly')
plt.ylabel('SPEI')
plt.legend()
plt.show()