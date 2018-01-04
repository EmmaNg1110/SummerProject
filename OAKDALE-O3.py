#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:56:35 2018

@author: emma

Site: Oakdale - Ozone
"""

import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np

#Read the file
file_new = '/home/emma/Documents/BargoChulloraOakdale1996to2017.csv'

# read file using pandas (pd)

df = pd.read_csv(file_new, sep=',', error_bad_lines=False, index_col=False)

df['date'] = pd.to_datetime(df['date'])
df['mon'] = df['date'].dt.month

df = df.set_index('date')

OAKDALE_O3 = df['OAKDALE OZONE ']*10.0

plt.plot(OAKDALE_O3, '.',color='g')

#Labelling 
plt.xlabel('time')
plt.ylabel('O3')
plt.show()



df_mm = df.resample('M').mean()
plt.plot(df_mm['OAKDALE OZONE '], '.',color='g')
plt.show()



new1 = df_mm.to_period(freq='M')

new1['OAKDALE OZONE '] = new1['OAKDALE OZONE ']*10.0

for i in range (1,13): 
    rolling = new1[['OAKDALE OZONE ']][new1.mon==i].rolling(window = 3, center=True)

    rolling_mean = rolling.mean()
    
    # plot original and transformed dataset
    
    rolling_mean['OAKDALE OZONE '].plot(label='Moving ave')
    
    #Index only O3 column, then mon==1 is just getting the Jan column from that 
    new1['OAKDALE OZONE '][new1.mon==i].plot(label='Raw')
    
    #anomoly = raw data - moving average 
    anomoly = (new1['OAKDALE OZONE '][new1.mon==i]) - rolling_mean['OAKDALE OZONE ']
    
    anomoly.plot(label='Anomaly')
    
    #print(anomoly,new1['O3'][new1.mon==i], rolling_mean['O3'])
    
    #Labelling
    plt.xlabel('date')
    plt.ylabel('ppbv')
    plt.grid(True)
    plt.legend()
    plt.title(i)
    plt.savefig("OAKDALE_O3_Month" + str(i) + ".png")
    plt.show()
    
#Putting all months together
    if i == 1:
        al1 = anomoly
        avg1 = rolling_mean[['OAKDALE OZONE ']]
        raw1 =  new1['OAKDALE OZONE '][new1.mon==i]
    else:
        temp = anomoly
        al1 = pd.concat([al1, temp])
        
        temp = rolling_mean[['OAKDALE OZONE ']]
        avg1 = pd.concat([avg1, temp])
        
        temp = new1['OAKDALE OZONE '][new1.mon==i]
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
plt.ylabel('ppbv')
plt.grid(True)
plt.legend(loc='best')
plt.title('OAKDALE_O3')
plt.savefig("OAKDALE_O3_Allmonths.png")
plt.show()