# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:32:31 2024


Generate the rise time, make corrections as well.

@author: jetbf
"""

import pandas as pd
import math


#constants for system bandwidth

SYSTEM_RISE_TIME = (0.35)/70000000
PROBE_RISE_TIME = (0.35)/100000000



#get file location to change
user = input()
target = "data_files//" + user + ".csv"

#read csv file
df = pd.read_csv(target)


#TInitial
tInitial = 10

#find TFinal
tFinal = 0
while tFinal < df.shape[0]:
    if df.at[tFinal, 'Volt2'] >= 2.97:
        break
    else:
        tFinal += 1


#output delta time
deltaTime = tFinal - tInitial
print(deltaTime, "microseconds")

#output corrected delta time
deltaTimeCorrected = math.sqrt((deltaTime**2) + (SYSTEM_RISE_TIME**2) + (PROBE_RISE_TIME**2))
print(deltaTimeCorrected, "microseconds, corrected")


#apply changes

