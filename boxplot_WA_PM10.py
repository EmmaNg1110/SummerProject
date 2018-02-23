#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:22:42 2018

@author: emma
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
import seaborn
from scipy import stats
seaborn.set(style="ticks")


#Read the file
file_new = '/home/emma/Downloads/cav11.csv'

# read file using pandas (pd)

df = pd.read_csv(file_new, sep=',', error_bad_lines=False, index_col=False)

df['date'] = pd.to_datetime(df['date'])


df2 = read_csv('/home/emma/Downloads/cav90.csv')

df2['date'] = pd.to_datetime(df2['date'])



frames = [df2[['date', 'PM10']], df[['date', 'PM10']]]

data = pd.concat(frames)

data['date'] = pd.to_datetime(data['date'])

data['mon'] = data['date'].dt.month

data = data.set_index('date')

data_mm = data.resample('M').mean()



#Read the file
file_new = '/home/emma/Downloads/dun11.csv'

# read file using pandas (pd)

df3 = pd.read_csv(file_new, sep=',', error_bad_lines=False, index_col=False)

df3['date'] = pd.to_datetime(df3['date'])


df4 = read_csv('/home/emma/Downloads/dun94.csv')

df4['date'] = pd.to_datetime(df2['date'])

#df4['PM10'] = df4['PM10'].convert_objects(convert_numeric=True)



frames = [df4[['date', 'PM10']], df3[['date', 'PM10']]]

data2 = pd.concat(frames)

data2['date'] = pd.to_datetime(data2['date'])

data2['mon'] = data2['date'].dt.month

data2 = data2.set_index('date')

#data2['PM10'] = data2['PM10'].convert_objects(convert_numeric=True)

data_mm2 = data2.resample('M').mean()


#Read the file
file_new = '/home/emma/Downloads/slk11.csv'

# read file using pandas (pd)

df5 = pd.read_csv(file_new, sep=',', error_bad_lines=False, index_col=False)

df5['date'] = pd.to_datetime(df5['date'])


df6 = read_csv('/home/emma/Downloads/slk00.csv')

df6['date'] = pd.to_datetime(df6['date'])

#df6['PM10'] = df6['PM10'].convert_objects(convert_numeric=True)



frames = [df6[['date', 'PM10']], df5[['date', 'PM10']]]

data3 = pd.concat(frames)

data3['date'] = pd.to_datetime(data3['date'])

data3['mon'] = data3['date'].dt.month

data3 = data3.set_index('date')

#data3['PM10'] = data3['PM10'].convert_objects(convert_numeric=True)

data_mm3 = data3.resample('M').mean()



new1 = data_mm.to_period(freq='M')
new2 = data_mm2.to_period(freq='M')
new3 = data_mm3.to_period(freq='M')


for i in range (1,13): 
    rolling = new1[['PM10']][new1.mon==i].rolling(window = 7, center=True)
    rolling_mean = rolling.mean()
    anomoly = (new1['PM10'][new1.mon==i]) - rolling_mean['PM10']
    
    rolling2 = new2[['PM10']][new2.mon==i].rolling(window = 7, center=True)
    rolling_mean2 = rolling2.mean()
    anomoly2 = (new2['PM10'][new2.mon==i]) - rolling_mean2['PM10']
    
    rolling3 = new3[['PM10']][new3.mon==i].rolling(window = 7, center=True)
    rolling_mean3 = rolling3.mean()
    anomoly3 = (new3['PM10'][new3.mon==i]) - rolling_mean3['PM10']


#Putting all months together
    if i == 1:
        al1 = anomoly
        al2 = anomoly2
        al3 = anomoly3
        
    else:
        temp = anomoly
        al1 = pd.concat([al1, temp])
        
        temp = anomoly2
        al2 = pd.concat([al2, temp])
        
        temp = anomoly3
        al3 = pd.concat([al3, temp])
        
al1=al1.sort_index()
al2=al2.sort_index()
al3=al3.sort_index()

al1 = al1.reset_index()
al2 = al2.reset_index()
al3 = al3.reset_index()

#Opening an NETCDF File
dataset = xr.open_dataset('/home/emma/Downloads/spei01.nc')


#Plotting Liverpool with a latitude of -33.9 and a longtitude of 150.1
spei = dataset.spei

#Swanbourne
spei_site1 = spei.sel(lat=-31.956,lon=115.762,method='nearest')

spei_site2 = spei.sel(lat=-31.6953,lon=116.3186,method='nearest')

spei_site3 = spei.sel(lat=-31.875,lon=115.975,method='nearest')

start_date1='1990-01'

end_date1='2016-01'

start_date2='1994-01'

end_date2='2016-01'

start_date3='2000-01'

end_date3='2016-01'

spei_site1 = spei_site1.sel(time=slice(start_date1,end_date1))
spei_site2 = spei_site2.sel(time=slice(start_date2,end_date2))
spei_site3 = spei_site3.sel(time=slice(start_date3,end_date3))

data1 = spei_site1.to_dataframe()
data2 = spei_site2.to_dataframe()
data3 = spei_site3.to_dataframe()

data1 = data1.reset_index()
data2 = data2.reset_index()
data3 = data3.reset_index()

result1 = pd.concat([data1['spei'], al1['PM10']], axis=1)
result2 = pd.concat([data2['spei'], al2['PM10']], axis=1)
result3 = pd.concat([data3['spei'], al3['PM10']], axis=1)


wet1 = result1[['spei', 'PM10']][data1.spei > 1.3]
wet2 = result2[['spei', 'PM10']][data2.spei > 1.3]
wet3 = result3[['spei', 'PM10']][data3.spei > 1.3]


drought1 = result1[['spei', 'PM10']][data1.spei < -1.3]
drought2 = result2[['spei', 'PM10']][data2.spei < -1.3]
drought3 = result3[['spei', 'PM10']][data3.spei < -1.3]

normal1 = result1[result1['spei'].between(-0.5, 0.5, inclusive=True)]
normal2 = result2[result2['spei'].between(-0.5, 0.5, inclusive=True)]
normal3 = result3[result3['spei'].between(-0.5, 0.5, inclusive=True)]


to_plot1 = drought1.append([drought2, drought3], ignore_index=True)

#to_plot2 = to_plot1["PM10"].append([to_plot1["PM10"]])


to_plot3 = normal1.append([normal2, normal3], ignore_index=True)

#to_plot4 = to_plot3["PM10"].append([to_plot3["PM10"]])


to_plot5 = wet1.append([wet2, wet3], ignore_index=True)

#to_plot6 = to_plot5["PM10"].append([to_plot5["PM10"]])
#mask =  ~np.isnan(to_plot2) & ~np.isnan(to_plot4)


data_to_plot = pd.concat([to_plot1['PM10'][~np.isnan(to_plot1['PM10'])], to_plot3['PM10'][~np.isnan(to_plot3['PM10'])], to_plot5['PM10'][~np.isnan(to_plot5['PM10'])]], axis=1, keys=['0','1','2'])

# Create a figure instance
figure = plt.figure(1, figsize=(7, 5))


# Create an axes instance
axes = figure.add_subplot(111)


# Create the boxplot
bp = axes.boxplot([data_to_plot['0'][~np.isnan(data_to_plot['0'])], data_to_plot['1'][~np.isnan(data_to_plot['1'])], data_to_plot['2'][~np.isnan(data_to_plot['2'])]], patch_artist=True, showmeans=True)

         
axes.set_xticklabels(['Drought', 'Normal', 'Wet'])
axes.set_ylim(-6.5, 5.5)
axes.set_ylabel('ppbv')
axes.set_title('PM10 Anomaly')

for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )
            
## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

# fill with colors
colors = ['darkorange', 'darkgrey', 'lightblue']
for bplot in (bp):
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

plt.axhline(y=0, linestyle=':')
plt.show()

#stats.ttest_ind(to_plot1['PM10'][~np.isnan(to_plot1['PM10'])],to_plot5['PM10'][~np.isnan(to_plot5['Ozone'])], equal_var = False)