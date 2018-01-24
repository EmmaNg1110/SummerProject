#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:33:39 2018

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


#Plotting BRINGELLYwith a latitude of -33.919444444444 and a longtitude of 150.76111111111
spei = dataset.spei

spei_site = spei.sel(lat=-33.919444444444,lon=150.76111111111,method='nearest')

#Start and end day of interested period, which is the same as the anomoly period

start_date='1994-01'

end_date='2016-01'

spei_site = spei_site.sel(time=slice(start_date,end_date))

spei_site.plot()


#Read the file
df = read_csv('/home/emma/Downloads/tmp_table_PM10_011996-012016.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['mon'] = df['Date'].dt.month

df = df.set_index('Date')


for i in range (1,13): 
    rolling = df[['BRINGELLY']][df.mon==i].rolling(window = 7, center=True)

    rolling_mean = rolling.mean()
    
    
    anomoly = (df['BRINGELLY'][df.mon==i]) - rolling_mean['BRINGELLY']


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
pyplot.title('BRINGELLY_PM10')
pyplot.show()



"""
 The two arrays we have both contain NAN values at various positions. 
 To do a linear regression on both to show how much the two arrays correlate:
 http://glowingpython.blogspot.de/2012/03/linear-regression-with-numpy.html
 However, the code line: slope, intercept, r_value, p_value, std_err = stats.linregress(varx, vary)
 results in nans for every output variable.
 
 --> Remove NaNs using a mask:
     mask = ~np.isnan(varx) & ~np.isnan(vary)
     slope, intercept, r_value, p_value, std_err = stats.linregress(varx[mask], vary[mask])
 
  The ~ operator means "is not", only for for NumPy arrays (it's an abuse of the normal meaning, which is the bitwise not operator). 
  See https://stackoverflow.com/questions/13600988/python-tilde-unary-operator-as-negation-numpy-bool-array/13602395#13602395
  
Source: https://stackoverflow.com/questions/13643363/linear-regression-of-arrays-containing-nans-in-python-numpy
"""

mask = ~np.isnan(spei_site) & ~np.isnan(al1)

RegressResult = stats.linregress(spei_site[mask], al1[mask])

slope, intercept, r_value, p_value, std_err = stats.linregress(spei_site[mask], al1[mask])

N = len(spei_site[mask])

print (RegressResult)
print (N)


#Plot the data along with the fitted line
plt.plot(spei_site, al1, 'o', label='Original Data')
plt.plot(spei_site, intercept + slope*spei_site, 'r', label='Fitted Line')
plt.xlabel('Anomoly')
plt.ylabel('SPEI')
plt.legend()
plt.show()