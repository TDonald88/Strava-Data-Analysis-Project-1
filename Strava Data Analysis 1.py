
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

Run_Data = pd.read_excel('YL_5K.xlsx', engine='openpyxl')# .astype('object')
#print(Run_Data)

X_axis = Run_Data['ns1:DistanceMeters2']
Y_axis = Run_Data['ns1:AltitudeMeters']
X_axis = X_axis/1609 # meters to miles
Y_axis = Y_axis*3.281 # meters to feet
Alt_min = np.min(Y_axis)

plt.plot(X_axis, Y_axis)
plt.title('Altitude over Distance')
plt.xlabel('Distance (miles)')
plt.ylabel('Altitude (feet)')
plt.fill_between(X_axis, Y_axis, np.min(Y_axis), color='green')
plt.show()




