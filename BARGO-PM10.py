#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:33:09 2018

@author: emma
"""

import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np

#Read the file
file_new = '/home/emma/Documents/BargoChulloraOakdale1996to2017.csv'

# read file using pandas (pd)

df = pd.read_csv(file_new, sep=',', error_bad_lines=False, index_col=False, encoding="utf-8-sig")

df['date'] = pd.to_datetime(df['date'])
df['mon'] = df['date'].dt.month

df = df.set_index('date')


Bargo_PM2 = df['BARGO PM10 ']

plt.plot(Bargo_PM2, '.',color='g')

#Labelling 
plt.xlabel('time')
plt.ylabel('PM10')
plt.show()



df_mm = df.resample('M').mean()
plt.plot(df_mm['BARGO PM10 '], '.',color='g')
plt.show()


new = df_mm.to_period(freq='M')

for i in range (1,13): 
    rolling = new[['BARGO PM10 ']][new.mon==i].rolling(window = 3, center=True)

    rolling_mean = rolling.mean()
    
    # plot original and transformed dataset
    
    rolling_mean['BARGO PM10 '].plot(label='Moving ave')
    
    #Index only PM10 column, then mon==1 is just getting the Jan column from that 
    new['BARGO PM10 '][new.mon==i].plot(label='Raw')
    
    #anomoly = raw data - moving average 
    anomoly = (new['BARGO PM10 '][new.mon==i]) - rolling_mean['BARGO PM10 ']
    
    anomoly.plot(label='Anomaly')
    
    #print(anomoly,new['PM10'][new.mon==i], rolling_mean['PM10'])
    
    #Labelling
    plt.xlabel('date')
    plt.ylabel('ug/m3')
    plt.grid(True)
    plt.legend()
    plt.title(i)
    plt.savefig("BARGO_PM10_Month" + str(i) + ".png")
    plt.show()
    
#Putting all months together
    if i == 1:
        al1 = anomoly
        avg1 = rolling_mean[['BARGO PM10 ']]
        raw1 =  new['BARGO PM10 '][new.mon==i]
    else:
        temp = anomoly
        al1 = pd.concat([al1, temp])
        
        temp = rolling_mean[['BARGO PM10 ']]
        avg1 = pd.concat([avg1, temp])
        
        temp = new['BARGO PM10 '][new.mon==i]
        raw1 = pd.concat([raw1, temp])

#sorting the entire dataframe according to index
avg1=avg1.sort_index()
al1=al1.sort_index()
raw1 = raw1.sort_index()

#Labelling
avg1.plot(label='Moving avg')
raw1.plot(label='Raw')
al1.plot(label='Anomoly')
plt.xlabel('date')
plt.ylabel('ug/m3')
plt.grid(True)
plt.legend(loc='best')
plt.title('BARGO_PM10')
plt.savefig("BARGO_PM10_Allmonths.png")
plt.show()

