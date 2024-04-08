# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:13:45 2024

This is used to make sure you have the correct file before modifying it!

@author: jetbf
"""

import pandas as pd

#get file location to change
user = input()

target = "data_files//" + user + ".csv"

#outputs information about file
df = pd.read_csv(target)
print(df.shape[0])
print(df.head(3))