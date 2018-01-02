#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:18:59 2017

@author: emma
"""

import pandas as pd

#import numpy as np

import matplotlib.pyplot as plt

#import scipy.stats as stats

# specify filename to read 

file_new = '/home/emma/Documents/2005_2015_long_format.csv'

# read file using pandas (pd)

df= pd.read_csv(file_new)

#Convert timestamp to datetime.date 

df['date'] = pd.to_datetime(df['date'])

#Seperating sites into Chullora, Earlwood, Lindfield, etc.
new1 = df.loc[df['site'] == 'Chullora']
new2 = df.loc[df['site'] == 'Earlwood']
new3 = df.loc[df['site'] == 'Lindfield']
new4 = df.loc[df['site'] == 'Liverpool']
new5 = df.loc[df['site'] == 'Prospect']
new6 = df.loc[df['site'] == 'Rozelle']

#Plot them against date
plt.plot(new1['date'], new1['O3'], '.',color='g')
plt.plot(new2['date'], new2['O3'], '.',color='r')
plt.plot(new3['date'], new3['O3'], '.',color='b')
plt.plot(new4['date'], new4['O3'], '.',color='k')
plt.plot(new5['date'], new5['O3'], '.',color='y')
plt.plot(new6['date'], new6['O3'], '.',color='m')

#Labelling 
plt.xlabel('time')
plt.ylabel('O3')
plt.grid(True)
plt.show()

#Monthly mean of Chullora
new1 = new1.set_index('date')
new1 = new1.resample('M').mean()

#Monthly mean of Earlwood
new2 = new2.set_index('date')
new2 = new2.resample('M').mean()

#Monthly mean of Lindfield
new3 = new3.set_index('date')
new3 = new3.resample('M').mean()

new4 = new4.set_index('date')
new4 = new4.resample('M').mean()

new5 = new5.set_index('date')
new5 = new5.resample('M').mean()

new6 = new6.set_index('date')
new6 = new6.resample('M').mean()

#Plot them together
plt.plot(new1['O3'], '.',color='g')
plt.plot(new2['O3'], '.',color='r')
plt.plot(new3['O3'], '.',color='b')
plt.plot(new4['O3'], '.',color='k')
plt.plot(new5['O3'], '.',color='y')
plt.plot(new6['O3'], '.',color='m')

#Labelling
plt.xlabel('time')
plt.ylabel('O3')
plt.grid(True)
plt.show()
