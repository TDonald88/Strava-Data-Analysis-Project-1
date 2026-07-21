
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

print("aight")

path = os.path.realpath(__file__)
dir = os.path.dirname(path)

dir = dir.replace('Strava Data Analysis Project 1', 'Run Data')

print(dir)
os.chdir(dir)

Run_Data = pd.read_excel('YL_5K.xlsx', engine='openpyxl')
print(Run_Data)

X_axis = Run_Data['ns1:Time']
Y_axis = Run_Data['ns2:Speed']

plt.plot(X_axis, Y_axis)
plt.show()




