# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:45:30 2024

This program averages out the Volt2 line between three files and then
saves the changes to a specified target file.

@author: jetbf
"""

import pandas as pd


#get file locations to change
print("Enter the name of the first file: ")
user = input()
target1 = "data_files//" + user + ".csv"

print("Enter the name of the second file: ")
user = input()
target2 = "data_files//" + user + ".csv"

print("Enter the name of the thrid file: ")
user = input()
target3 = "data_files//" + user + ".csv"

#specify desination file, make this file beforehand.
print("Which file do you want to save the final result to: ")
user = input()
target = "data_files//" + user + ".csv"

"""
print("How many lines of data: ")
count = input()
"""

#read csv file
df1 = pd.read_csv(target1)
df2 = pd.read_csv(target2)
df3 = pd.read_csv(target3)
df = pd.read_csv(target)

#print for proof
print("Before: ")
print(df1.head(3), "\n", 
      df2.head(3), "\n",
      df3.head(3))






#a loop that will average out the 'Volt2' column
#then, it will save it to the target destination file
i = 0
while i < df.shape[0]:
    a = df1.at[i, 'Volt2']
    b = df2.at[i, 'Volt2']
    c = df3.at[i, 'Volt2']
    
    df.at[i, 'Volt2'] = (a+b+c)/3
    
    i += 1
    
#apply changes
df.to_csv(target, index=False)

#print for proof
print("\nAfter: ")
print(df1.head(3), "\n", 
      df2.head(3), "\n",
      df3.head(3), "\n",
      df.head(3))

