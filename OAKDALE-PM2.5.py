#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:37:03 2018

@author: emma

Site: Oakdale - PM2.5
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


OAKDALE_PM2 = df['OAKDALE PM2.5 ']

plt.plot(OAKDALE_PM2, '.',color='g')

#Labelling 
plt.xlabel('time')
plt.ylabel('PM2.5')
plt.show()



df_mm = df.resample('M').mean()
plt.plot(df_mm['OAKDALE PM2.5 '], '.',color='g')
plt.show()


new = df_mm.to_period(freq='M')

for i in range (1,13): 
    rolling = new[['OAKDALE PM2.5 ']][new.mon==i].rolling(window = 3, center=True)

    rolling_mean = rolling.mean()
    
    # plot original and transformed dataset
    
    rolling_mean['OAKDALE PM2.5 '].plot(label='Moving ave')
    
    #Index only PM2.5 column, then mon==1 is just getting the Jan column from that 
    new['OAKDALE PM2.5 '][new.mon==i].plot(label='Raw')
    
    #anomoly = raw data - moving average 
    anomoly = (new['OAKDALE PM2.5 '][new.mon==i]) - rolling_mean['OAKDALE PM2.5 ']
    
    anomoly.plot(label='Anomaly')
    
    #print(anomoly,new['PM2.5'][new.mon==i], rolling_mean['PM2.5'])
    
    #Labelling
    plt.xlabel('date')
    plt.ylabel('ug/m3')
    plt.grid(True)
    plt.legend()
    plt.title(i)
    plt.savefig("OAKDALE_PM2.5_Month" + str(i) + ".png")
    plt.show()
    
#Putting all months together
    if i == 1:
        al1 = anomoly
        avg1 = rolling_mean[['OAKDALE PM2.5 ']]
        raw1 =  new['OAKDALE PM2.5 '][new.mon==i]
    else:
        temp = anomoly
        al1 = pd.concat([al1, temp])
        
        temp = rolling_mean[['OAKDALE PM2.5 ']]
        avg1 = pd.concat([avg1, temp])
        
        temp = new['OAKDALE PM2.5 '][new.mon==i]
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
plt.title('OAKDALE_PM2.5')
plt.savefig("OAKDALE_PM2.5_Allmonths.png")
plt.show()

