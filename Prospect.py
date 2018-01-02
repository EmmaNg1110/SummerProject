#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:50:15 2018

@author: emma

Site: Prospect
"""

from pandas import read_csv
import pandas as pd
from matplotlib import pyplot

#Read the file
df = read_csv('/home/emma/Documents/2005_2015_long_format.csv')

df['date'] = pd.to_datetime(df['date'])
df['mon'] = df['date'].dt.month

#Seperating sites into Prospect
new5 = df.loc[df['site'] == 'Prospect']

#Monthly mean of Prospect
new5 = new5.set_index('date')
new5 = new5.resample('M').mean()

#But our data are monthly means, so they are related not to some particular 
#point in time, but rather to the time interval, or time span. 
#We can convert time stamps in our Series to time periods, and then combine them.
new5 = new5.to_period(freq='M')


# Tail-rolling average transform for O3

for i in range (1,13): 
    rolling = new5[['O3']][new5.mon==i].rolling(window = 3, center=True)

    rolling_mean = rolling.mean()
    
    # plot original and transformed dataset
    
    rolling_mean['O3'].plot(label='Moving ave')
    
    #Index only O3 column, then mon==1 is just getting the Jan column from that 
    new5['O3'][new5.mon==i].plot(label='Raw')
    
    #anomoly = raw data - moving average 
    anomoly = (new5['O3'][new5.mon==i]) - rolling_mean['O3']
    
    anomoly.plot(label='Anomaly')
    
    #print(anomoly,new5['O3'][new5.mon==i], rolling_mean['O3'])
    
    #Labelling
    pyplot.xlabel('date')
    pyplot.ylabel('ppbv')
    pyplot.grid(True)
    pyplot.legend()
    pyplot.title(i)
    pyplot.savefig("Prospect_O3_Month" + str(i) + ".png")
    pyplot.show()
    
#Putting all months together
    if i == 1:
        al1 = anomoly
        avg1 = rolling_mean[['O3']]
        raw1 =  new5['O3'][new5.mon==i]
    else:
        temp = anomoly
        al1 = pd.concat([al1, temp])
        
        temp = rolling_mean[['O3']]
        avg1 = pd.concat([avg1, temp])
        
        temp = new5['O3'][new5.mon==i]
        raw1 = pd.concat([raw1, temp])

#sorting the entire dataframe according to index
avg1=avg1.sort_index()
al1=al1.sort_index()
raw1 = raw1.sort_index()

#Labelling
avg1.plot(label='Moving avg')
raw1.plot(label='Raw')
al1.plot(label='Anomoly')
pyplot.xlabel('date')
pyplot.ylabel('ppbv')
pyplot.grid(True)
pyplot.legend(loc='best')
pyplot.title('Prospect_O3')
pyplot.savefig("Prospect_O3_Allmonths.png")
pyplot.show()


# Tail-rolling average transform for PM2.5
for j in range (1,13): 
    rolling2 = new5[['PM2.5']][new5.mon==j].rolling(window = 3, center=True)

    rolling_mean2 = rolling2.mean()
    
    # plot original and transformed dataset
    
    rolling_mean2['PM2.5'].plot(label='Moving ave')
    
    #Index only PM2.5 column, then mon==1 is just getting the Jan column from that 
    new5['PM2.5'][new5.mon==j].plot(label='Raw')
    
    #anomoly = raw data - moving average 
    anomoly2 = (new5['PM2.5'][new5.mon==j]) - rolling_mean2['PM2.5']
    
    anomoly2.plot(label='Anomaly')
    
    #print(anomoly,new5['PM2.5'][new5.mon==i], rolling_mean['PM2.5'])
    
    #Labelling
    pyplot.xlabel('date')
    pyplot.ylabel('ppbv')
    pyplot.grid(True)
    pyplot.legend()
    pyplot.title(j)
    pyplot.savefig("Prospect_PM2.5_Month" + str(j) + ".png")
    pyplot.show()
    
#Putting all months together
    if j == 1:
        al = anomoly2
        avg = rolling_mean2[['PM2.5']]
        raw =  new5['PM2.5'][new5.mon==j]
    else:
        temp = anomoly2
        al = pd.concat([al, temp])
        
        temp = rolling_mean2[['PM2.5']]
        avg = pd.concat([avg, temp])
        
        temp = new5['PM2.5'][new5.mon==j]
        raw = pd.concat([raw, temp])

#sorting the entire dataframe according to index
avg=avg.sort_index()
al=al.sort_index()
raw = raw.sort_index()

#Labelling
avg.plot(label='Moving avg')
raw.plot(label='Raw')
al.plot(label='Anomoly')
pyplot.xlabel('date')
pyplot.ylabel('ppbv')
pyplot.grid(True)
pyplot.legend(loc='best')
pyplot.title('Prospect_PM2.5')
pyplot.savefig("Prospect_PM2.5_Allmonths.png")
