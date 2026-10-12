
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

first_valid = np.flatnonzero(Dist != 0)[0]
Pace_clean = Pace[first_valid:].to_numpy()
Dist_clean = Dist[first_valid:].to_numpy()

Splits = []

for n in range(int(np.floor(Dist_clean.min())), int(np.ceil(Dist_clean.max())) + 1):
    index = np.where((Dist_clean >= n) & (Dist_clean < n + 1))[0]
    if len(index) > 0:
        Splits.append(float(Pace_clean[index].mean()))


print(Splits)

Splits_displ = np.array(Splits, dtype = float)
Splits_displ = np.floor(Splits_displ)
Splits_rem = np.int32(60 * (Splits - Splits_displ))
Splits_displ1 = np.array([f"{int(m)}:{s:02d}" for m, s in zip(Splits_displ, Splits_rem)],
                         dtype = object)
print(Splits_displ1)

Mile_Markers = np.arange(1, Tot_dist + 1, 1)
Mile_Markers[Mile_Markers == np.max(Mile_Markers)] = Tot_dist
Mile_Markers = np.round(Mile_Markers, 3)
print(Mile_Markers)

bar_positions = np.arange(len(Splits))

bars = plt.bar(bar_positions, Splits)
plt.bar_label(bars, labels = Splits_displ1)
plt.xticks(bar_positions, Mile_Markers) # labels = mile markers
plt.title('Splits')
plt.xlabel('Distance (miles)')
plt.ylabel('Pace (min/mile)')
plt.show()






