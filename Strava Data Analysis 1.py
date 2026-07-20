
import numpy as np
import pandas as pd
import os

print("aight")

path = os.path.realpath(__file__)
dir = os.path.dirname(path)

dir = dir.replace('Strava Data Analysis Project 1', 'Run Data')

print(dir)
os.chdir(dir)

Data_read = pd.read_excel('YL_5K.xlsx', engine='openpyxl')
print(Data_read)



