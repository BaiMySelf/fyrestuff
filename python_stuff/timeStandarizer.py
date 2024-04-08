# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:13:04 2024

This is used to alter the time to microseconds, something a
human can actually read.

@author: jetbf
"""

import pandas as pd


#get file location to change
user = input()
target = "data_files//" + user + ".csv"

#read csv file
df = pd.read_csv(target)

#print for proof
print("Before: ")
print(df.head(3))

#while loop to change 'second' value to something I understand
i = 0
while i < df.shape[0]:
    df.at[i, 'second'] = i
    i += 1
#apply that change
df.to_csv(target, index=False)

#print for proof
print("After: ")
print(df.head(3))

