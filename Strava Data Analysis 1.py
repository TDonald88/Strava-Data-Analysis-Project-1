
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

# ------------ Altitude over distance ----------

X_axis = Run_Data['ns1:DistanceMeters2']
Y_axis = Run_Data['ns1:AltitudeMeters']
X_axis = X_axis/1609 # meters to miles
Y_axis = Y_axis*3.281 # meters to feet

plt.plot(X_axis, Y_axis)
plt.title('Altitude over Distance')
plt.xlabel('Distance (miles)')
plt.ylabel('Altitude (feet)')
plt.fill_between(X_axis, Y_axis, np.min(Y_axis), color='green')
plt.show()


Time1 = Run_Data['ns1:Time'].str.replace({"2026-06-06T": "",
                                         "Z": ""})
# print(Time1)

# ---------- Pace over distance ----------

Dist = Run_Data['ns1:DistanceMeters2']/1609 #in miles

Pace = Run_Data['ns2:Speed'] * (60/1609)
Pace[Pace != 0] = 1/Pace

plt.plot(Dist, Pace)
plt.ylim(13, 2)
plt.title('Pace Over Distance')
plt.xlabel('Distance (miles)')
plt.ylabel('Pace (min/mile)')
plt.show()

# ---------- Splits -----------

Tot_dist = np.max(Dist)
Avg_Pace = np.mean(Pace)
print(Avg_Pace)

#for i in range(len(Dist)):
#    if Dist[i] > 

#print(Splits)


