# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:56:12 2024

The framework for turning csv files into graphs!

Should make another program for including multiple lines

@author: jetbf
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#get file location to change
user = input()
target = "data_files//" + user + ".csv"

#read csv file
df = pd.read_csv(target)

#create the graph! might also try scatterplot
plt.errorbar(df['second'], df['Volt2'], 0.05, 0, errorevery = 5)

#plt.plot(df['second'], df['Volt2'])

plt.title("HCPL0701 Optocoupler\nwith 270Ω Pull-Up Resistor", loc = 'center')

plt.grid(1, linestyle = ':')

#plt.legend(handles = [second, Volt2], loc = 'lower right')

plt.ylabel("Volt (V)", loc = 'center')
plt.xlabel("Time (μs)", loc = 'center')

plt.margins(x = 0, y = 0)





#lines to designate TInitial and VLow
plt.vlines(10, 0, df.at[10, 'Volt2'], 'black', 'dashed', "TInitial")
plt.hlines(df.at[10, 'Volt2'], 0, 10, 'black', 'dashed', "VLow")


#find TFinal
tFinal = 0
while tFinal < df.shape[0]:
    if df.at[tFinal, 'Volt2'] >= 2.97:
        break
    else:
        tFinal += 1
    
#lines to designate TFinal and VHigh
plt.vlines(tFinal, 0, df.at[tFinal, 'Volt2'], 'black', 'dashed', 'TFinal')
plt.hlines(df.at[tFinal, 'Volt2'], 0, tFinal, 'black', 'dashed', 'VHigh')