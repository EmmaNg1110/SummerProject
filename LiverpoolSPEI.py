#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:59:11 2018

@author: emma
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
from matplotlib import pyplot
from datetime import date
from scipy.stats import linregress

dataset = xr.open_dataset('/home/emma/Downloads/spei01.nc')
df = dataset.to_dataframe()

spei=dataset.spei

spei_site = spei.sel(lat=-33.9,lon=150.1,method='nearest')

start_date='2006-01'

end_date='2015-01'

spei_site = spei_site.sel(time=slice(start_date,end_date))

spei_site.plot()



df = read_csv('/home/emma/Documents/2005_2015_long_format.csv')

df['date'] = pd.to_datetime(df['date'])
df['mon'] = df['date'].dt.month

#Seperating sites into Chullora
new4 = df.loc[df['site'] == 'Liverpool']

#Monthly mean of Chullora
new4 = new4.set_index('date')
new4 = new4.resample('M').mean()

#But our data are monthly means, so they are related not to some particular 
#point in time, but rather to the time interval, or time span. 
#We can convert time stamps in our Series to time periods, and then combine them.
new4 = new4.to_period(freq='M')

for i in range (1,13): 
    rolling = new4[['O3']][new4.mon==i].rolling(window = 3, center=True)

    rolling_mean = rolling.mean()
    
  
    #anomoly = raw data - moving average 
    anomoly = (new4['O3'][new4.mon==i]) - rolling_mean['O3']
    
    
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
pyplot.title('Liverpool_O3')
pyplot.show()

linregress(spei_site, al1)
print (linregress)