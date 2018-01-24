#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:16:35 2018

@author: emma
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
import seaborn
seaborn.set(style="ticks")

#Read the file
df = read_csv('/home/emma/Downloads/tmp_table_Ozone_1houravg_011996-012016.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['mon'] = df['Date'].dt.month

df = df.set_index('Date')

df = df.reset_index()



#AlP = df['ALBION PARK STH ']*10.0
Bargo = df['BARGO ']*10.0
Liv = df['LIVERPOOL']*10.0
Bringelly = df['BRINGELLY']*10.0
Chullora = df['CHULLORA ']*10.0
Earlwood = df['EARLWOOD']*10.0
KemGr = df['KEMBLA GRANGE']*10.0
Lindfield = df['LINDFIELD ']*10.0
#Newcastle = df['NEWCASTLE']*10.0
Oakdale = df['OAKDALE ']*10.0
#Prospect = df['PROSPECT ']*10.0
#Randwick = df['RANDWICK ']*10.0
Rozelle = df['ROZELLE ']*10.0
StMarys = df['ST MARYS']*10.0
#Wallsend = df['WALLSEND']*10.0


for i in range (1,13): 
    
#    rolling = AlP[df.mon==i].rolling(window = 5, center=True)
#    rolling_mean = rolling.mean()    
#    anomoly = (AlP[df.mon==i]) - rolling_mean
    
    
    rolling2 = Bargo[df.mon==i].rolling(window = 7, center=True)
    rolling_mean2 = rolling2.mean()
    anomoly2 = (Bargo[df.mon==i]) - rolling_mean2


    rolling3 = Liv[df.mon==i].rolling(window = 7, center=True)
    rolling_mean3 = rolling3.mean()
    anomoly3 = (Liv[df.mon==i]) - rolling_mean3
    
    
    rolling4 = Bringelly[df.mon==i].rolling(window = 7, center=True)
    rolling_mean4 = rolling4.mean()
    anomoly4 = (Bringelly[df.mon==i]) - rolling_mean4
    
    
    rolling5 = Chullora[df.mon==i].rolling(window = 7, center=True)
    rolling_mean5 = rolling5.mean()
    anomoly5 = (Chullora[df.mon==i]) - rolling_mean5
    
    
    rolling6 = Earlwood[df.mon==i].rolling(window = 7, center=True)
    rolling_mean6 = rolling6.mean()
    anomoly6 = (Earlwood[df.mon==i]) - rolling_mean6
    
    
    rolling7 = KemGr[df.mon==i].rolling(window = 7, center=True)
    rolling_mean7 = rolling7.mean()
    anomoly7 = (KemGr[df.mon==i]) - rolling_mean7
    
    
    rolling8 = Lindfield[df.mon==i].rolling(window = 7, center=True)
    rolling_mean8 = rolling8.mean()
    anomoly8 = (Lindfield[df.mon==i]) - rolling_mean8
    
    
#    rolling9 = Newcastle[df.mon==i].rolling(window = 7, center=True)
#    rolling_mean9 = rolling9.mean()
#    anomoly9 = (Newcastle[df.mon==i]) - rolling_mean9
    
    
    rolling10 = Oakdale[df.mon==i].rolling(window = 7, center=True)
    rolling_mean10 = rolling10.mean()
    anomoly10 = (Oakdale[df.mon==i]) - rolling_mean10
    
    
#    rolling11 = Prospect[df.mon==i].rolling(window = 7, center=True)
#    rolling_mean11 = rolling11.mean()
#    anomoly11 = (Prospect[df.mon==i]) - rolling_mean11
    
    
#    rolling12 = Randwick[df.mon==i].rolling(window = 7, center=True)
#    rolling_mean12 = rolling12.mean()
#    anomoly12 = (Randwick[df.mon==i]) - rolling_mean12
    
    
    rolling13 = Rozelle[df.mon==i].rolling(window = 7, center=True)
    rolling_mean13 = rolling13.mean()
    anomoly13 = (Rozelle[df.mon==i]) - rolling_mean13
    
    
    rolling14 = StMarys[df.mon==i].rolling(window = 7, center=True)
    rolling_mean14 = rolling14.mean()
    anomoly14 = (StMarys[df.mon==i]) - rolling_mean14
    
    
#    rolling15 = Wallsend[df.mon==i].rolling(window = 5, center=True)
#    rolling_mean15 = rolling15.mean()
#    anomoly15 = (Wallsend[df.mon==i]) - rolling_mean15
    
#Putting all months together
    if i == 1:
#        al1 = anomoly
        al2 = anomoly2
        al3 = anomoly3
        al4 = anomoly4
        al5 = anomoly5
        al6 = anomoly6
        al7 = anomoly7
        al8 = anomoly8
#        al9 = anomoly9
        al10 = anomoly10
#        al11 = anomoly11
#        al12 = anomoly12
        al13 = anomoly13
        al14 = anomoly14
#        al15 = anomoly15
        
    else:
#        temp = anomoly
#        al1 = pd.concat([al1, temp])
        
        temp = anomoly2
        al2 = pd.concat([al2, temp])
        
        temp = anomoly3
        al3 = pd.concat([al3, temp])
        
        temp = anomoly4
        al4 = pd.concat([al4, temp])

        temp = anomoly5
        al5 = pd.concat([al5, temp])
        
        temp = anomoly6
        al6 = pd.concat([al6, temp])
        
        temp = anomoly7
        al7 = pd.concat([al7, temp])
        
        temp = anomoly8
        al8 = pd.concat([al8, temp])
        
#        temp = anomoly9
#        al9 = pd.concat([al9, temp])
        
        temp = anomoly10
        al10 = pd.concat([al10, temp])
        
#        temp = anomoly11
#        al11 = pd.concat([al11, temp])
        
#        temp = anomoly12
#        al12 = pd.concat([al12, temp])
        
        temp = anomoly13
        al13 = pd.concat([al13, temp])
        
        temp = anomoly14
        al14 = pd.concat([al14, temp])
        
#        temp = anomoly15
#        al15 = pd.concat([al15, temp])

#sorting the entire dataframe according to index

#al1=al1.sort_index()
al2=al2.sort_index()
al3=al3.sort_index()
al4=al4.sort_index()
al5=al5.sort_index()
al6=al6.sort_index()
al7=al7.sort_index()
al8=al8.sort_index()
#al9=al9.sort_index()
al10=al10.sort_index()
#al11=al11.sort_index()
#al12=al12.sort_index()
al13=al13.sort_index()
al14=al14.sort_index()
#al15=al15.sort_index()


#Opening an NETCDF File
dataset = xr.open_dataset('/home/emma/Downloads/spei01.nc')


#Plotting Liverpool with a latitude of -33.9 and a longtitude of 150.1
spei = dataset.spei

#Alibion Park Sth
#spei_site1 = spei.sel(lat=-34.580555555556,lon=150.78166666667,method='nearest')
#Bargo
spei_site2 = spei.sel(lat=-34.3075,lon=150.58,method='nearest')
#Liverpool
spei_site3 = spei.sel(lat=-33.93277778,lon=150.90583333,method='nearest')
#Bringelly
spei_site4 = spei.sel(lat=-33.919444444444,lon=150.76111111111,method='nearest')
#Chullora
spei_site5 = spei.sel(lat=-33.89388889,lon=151.04527778,method='nearest')
#Earlwood
spei_site6 = spei.sel(lat=-33.91777778,lon=151.03472222,method='nearest')
#Kembla Grange
spei_site7 = spei.sel(lat=-34.476388888889,lon=150.8175,method='nearest')
#Lindfield
spei_site8 = spei.sel(lat=-33.93277778,lon=150.90583333,method='nearest')
#Newcastle
#spei_site9 = spei.sel(lat=-32.9325,lon=151.75833333333,method='nearest')
#Oakdale
spei_site10 = spei.sel(lat=-34.05305556,lon=150.49722222,method='nearest')
#Prospect
#spei_site11 = spei.sel(lat=-33.79472222,lon=150.9125,method='nearest')
#Randwick
#spei_site12 = spei.sel(lat=-33.933333333333,lon=151.24194444444,method='nearest')
#Rozelle
spei_site13 = spei.sel(lat=-33.86583333,lon=151.1625,method='nearest')
#StMarys
spei_site14 = spei.sel(lat=-33.797222222222,lon=150.8175,method='nearest')
#Wallsend
#spei_site15 = spei.sel(lat=-32.896111111111,lon=151.66916666667,method='nearest')


#Start and end day of interested period, which is the same as the anomoly period

start_date='1994-01'

end_date='2016-01'

#spei_site1 = spei_site1.sel(time=slice(start_date,end_date))
spei_site2 = spei_site2.sel(time=slice(start_date,end_date))
spei_site3 = spei_site3.sel(time=slice(start_date,end_date))
spei_site4 = spei_site4.sel(time=slice(start_date,end_date))
spei_site5 = spei_site5.sel(time=slice(start_date,end_date))
spei_site6 = spei_site6.sel(time=slice(start_date,end_date))
spei_site7 = spei_site7.sel(time=slice(start_date,end_date))
spei_site8 = spei_site8.sel(time=slice(start_date,end_date))
#spei_site9 = spei_site9.sel(time=slice(start_date,end_date))
spei_site10 = spei_site10.sel(time=slice(start_date,end_date))
#spei_site11 = spei_site11.sel(time=slice(start_date,end_date))
#spei_site12 = spei_site12.sel(time=slice(start_date,end_date))
spei_site13 = spei_site13.sel(time=slice(start_date,end_date))
spei_site14 = spei_site14.sel(time=slice(start_date,end_date))
#spei_site15 = spei_site15.sel(time=slice(start_date,end_date))


#data1 = spei_site1.to_dataframe()
data2 = spei_site2.to_dataframe()
data3 = spei_site3.to_dataframe()
data4 = spei_site4.to_dataframe()
data5 = spei_site5.to_dataframe()
data6 = spei_site6.to_dataframe()
data7 = spei_site7.to_dataframe()
data8 = spei_site8.to_dataframe()
#data9 = spei_site9.to_dataframe()
data10 = spei_site10.to_dataframe()
#data11 = spei_site11.to_dataframe()
#data12 = spei_site12.to_dataframe()
data13 = spei_site13.to_dataframe()
data14 = spei_site14.to_dataframe()
#data15 = spei_site15.to_dataframe()


#data1 = data1.reset_index()
data2 = data2.reset_index()
data3 = data3.reset_index()
data4 = data4.reset_index()
data5 = data5.reset_index()
data6 = data6.reset_index()
data7 = data7.reset_index()
data8 = data8.reset_index()
#data9 = data9.reset_index()
data10 = data10.reset_index()
#data11 = data11.reset_index()
#data12 = data12.reset_index()
data13 = data13.reset_index()
data14 = data14.reset_index()
#data15 = data15.reset_index()


#result1 = pd.concat([data1['spei'], al1], axis=1)
result2 = pd.concat([data2['spei'], al2], axis=1)
result3 = pd.concat([data3['spei'], al3], axis=1)
result4 = pd.concat([data4['spei'], al4], axis=1)
result5 = pd.concat([data5['spei'], al5], axis=1)
result6 = pd.concat([data6['spei'], al6], axis=1)
result7 = pd.concat([data7['spei'], al7], axis=1)
result8 = pd.concat([data8['spei'], al8], axis=1)
#result9 = pd.concat([data9['spei'], al9], axis=1)
result10 = pd.concat([data10['spei'], al10], axis=1)
#result11 = pd.concat([data11['spei'], al11], axis=1)
#result12 = pd.concat([data12['spei'], al12], axis=1)
result13 = pd.concat([data13['spei'], al13], axis=1)
result14 = pd.concat([data14['spei'], al14], axis=1)
#result15 = pd.concat([data15['spei'], al15], axis=1)


#wet1 = result1[['spei', 'ALBION PARK STH ']][data1.spei > 1.3]
wet2 = result2[['spei', 'BARGO ']][data2.spei > 1.3]
wet3 = result3[['spei', 'LIVERPOOL']][data3.spei > 1.3]
wet4 = result4[['spei', 'BRINGELLY']][data4.spei > 1.3]
wet5 = result5[['spei', 'CHULLORA ']][data5.spei > 1.3]
wet6 = result6[['spei', 'EARLWOOD']][data6.spei > 1.3]
wet7 = result7[['spei', 'KEMBLA GRANGE']][data7.spei > 1.3]
wet8 = result8[['spei', 'LINDFIELD ']][data8.spei > 1.3]
#wet9 = result9[['spei', 'NEWCASTLE']][data9.spei > 1.3]
wet10 = result10[['spei', 'OAKDALE ']][data10.spei > 1.3]
#wet11 = result11[['spei', 'PROSPECT ']][data11.spei > 1.3]
#wet12 = result12[['spei', 'RANDWICK ']][data12.spei > 1.3]
wet13 = result13[['spei', 'ROZELLE ']][data13.spei > 1.3]
wet14 = result14[['spei', 'ST MARYS']][data14.spei > 1.3]
#wet15 = result15[['spei', 'WALLSEND']][data15.spei > 1.3]


#drought1 = result1[['spei', 'ALBION PARK STH ']][data1.spei < -1.3]
drought2 = result2[['spei', 'BARGO ']][data2.spei < -1.3]
drought3 = result3[['spei', 'LIVERPOOL']][data3.spei < -1.3]
drought4 = result4[['spei', 'BRINGELLY']][data4.spei < -1.3]
drought5 = result5[['spei', 'CHULLORA ']][data5.spei < -1.3]
drought6 = result6[['spei', 'EARLWOOD']][data6.spei < -1.3]
drought7 = result7[['spei', 'KEMBLA GRANGE']][data7.spei < -1.3]
drought8 = result8[['spei', 'LINDFIELD ']][data8.spei < -1.3]
#drought9 = result9[['spei', 'NEWCASTLE']][data9.spei < -1.3]
drought10 = result10[['spei', 'OAKDALE ']][data10.spei < -1.3]
#drought11 = result11[['spei', 'PROSPECT ']][data11.spei < -1.3]
#drought12 = result12[['spei', 'RANDWICK ']][data12.spei < -1.3]
drought13 = result13[['spei', 'ROZELLE ']][data13.spei < -1.3]
drought14 = result14[['spei', 'ST MARYS']][data14.spei < -1.3]
#drought15 = result15[['spei', 'WALLSEND']][data15.spei < -1.3]



normal2 = result2[result2['spei'].between(-0.5, 0.5, inclusive=True)]
normal3 = result3[result3['spei'].between(-0.5, 0.5, inclusive=True)]
normal4 = result4[result4['spei'].between(-0.5, 0.5, inclusive=True)]
normal5 = result5[result5['spei'].between(-0.5, 0.5, inclusive=True)]
normal6 = result6[result6['spei'].between(-0.5, 0.5, inclusive=True)]
normal7 = result7[result7['spei'].between(-0.5, 0.5, inclusive=True)]
normal8 = result8[result8['spei'].between(-0.5, 0.5, inclusive=True)]
normal10 = result10[result10['spei'].between(-0.5, 0.5, inclusive=True)]
#normal11 = result11[result11['spei'].between(-0.5, 0.5, inclusive=True)]
normal13 = result13[result13['spei'].between(-0.5, 0.5, inclusive=True)]
normal14 = result14[result14['spei'].between(-0.5, 0.5, inclusive=True)]




to_plot1 = drought2.append([drought3, drought4, drought5, drought6, drought7, drought8, drought10, drought13, drought14], ignore_index=True)

to_plot2 = to_plot1["BARGO "].append([to_plot1["LIVERPOOL"], to_plot1["BRINGELLY"], to_plot1["CHULLORA "], to_plot1["EARLWOOD"], to_plot1["LINDFIELD "], to_plot1["OAKDALE "], to_plot1["ROZELLE "], to_plot1["ST MARYS"]])


to_plot3 = normal2.append([normal3, normal4, normal5, normal6, normal7, normal8, normal10, normal13, normal14], ignore_index=True)

to_plot4 = to_plot3["BARGO "].append([to_plot3["LIVERPOOL"], to_plot3["BRINGELLY"], to_plot3["CHULLORA "], to_plot3["EARLWOOD"], to_plot3["LINDFIELD "], to_plot3["OAKDALE "], to_plot3["ROZELLE "], to_plot3["ST MARYS"]])


to_plot5 = wet2.append([wet3, wet4, wet5, wet6, wet7, wet8, wet10, wet13, wet14], ignore_index=True)

to_plot6 = to_plot5["BARGO "].append([to_plot5["LIVERPOOL"], to_plot5["BRINGELLY"], to_plot5["CHULLORA "], to_plot5["EARLWOOD"], to_plot5["LINDFIELD "], to_plot5["OAKDALE "], to_plot5["ROZELLE "], to_plot5["ST MARYS"]])
#mask =  ~np.isnan(to_plot2) & ~np.isnan(to_plot4)


data_to_plot = pd.concat([to_plot2[~np.isnan(to_plot2)], to_plot4[~np.isnan(to_plot4)], to_plot6[~np.isnan(to_plot6)]], axis=1)


#data_to_plot = pd.concat([to_plot2[mask], to_plot4[mask]], axis=1)

# Create a figure instance
figure = plt.figure(1, figsize=(9, 6))


# Create an axes instance
ax = figure.add_subplot(111)

mask = ~np.isnan(data_to_plot[1])


# Create the boxplot
bp = ax.boxplot([data_to_plot[0][~np.isnan(data_to_plot[0])], data_to_plot[1][mask], data_to_plot[2][~np.isnan(data_to_plot[2])]], patch_artist=True)

         
ax.set_xticklabels(['Drought', 'Normal', 'Wet'])
ax.set_title('Ozone Anomoly')

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

plt.show()