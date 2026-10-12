
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
#plt.title('Altitude over Distance')
#plt.xlabel('Distance (miles)')
#plt.ylabel('Altitude (feet)')
#plt.fill_between(X_axis, Y_axis, np.min(Y_axis), color='green')
# plt.show()


Time1 = Run_Data['ns1:Time'].str.replace({"2026-06-06T": "",
                                         "Z": ""})
# print(Time1)

# ---------- Pace over distance ----------

Dist = Run_Data['ns1:DistanceMeters2']/1609 #in miles

Pace = Run_Data['ns2:Speed'] * (60/1609)
Pace[Pace != 0] = 1/Pace

#plt.plot(Dist, Pace)
#plt.ylim(13, 2)
#plt.title('Pace Over Distance')
#plt.xlabel('Distance (miles)')
#plt.ylabel('Pace (min/mile)')
# plt.show()

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


# print(Splits)

Splits_displ = np.array(Splits, dtype = float)
Splits_displ = np.floor(Splits_displ)
Splits_rem = np.int32(60 * (Splits - Splits_displ))
Splits_displ1 = np.array([f"{int(m)}:{s:02d}" for m, s in zip(Splits_displ, Splits_rem)],
                         dtype = object)
#print(Splits_displ1)

Mile_Markers = np.arange(1, Tot_dist + 1, 1)
Mile_Markers[Mile_Markers == np.max(Mile_Markers)] = Tot_dist
Mile_Markers = np.round(Mile_Markers, 3)
#print(Mile_Markers)

bar_positions = np.arange(len(Splits))

bars = plt.bar(bar_positions, Splits)
#plt.bar_label(bars, labels = Splits_displ1)
#plt.xticks(bar_positions, Mile_Markers) # labels = mile markers
#plt.title('Splits')
#plt.xlabel('Distance (miles)')
#plt.ylabel('Pace (min/mile)')
# plt.show()

# ---------- Map --------------------------

Latitude = Run_Data['ns1:LatitudeDegrees'].to_numpy()
Longitude = Run_Data['ns1:LongitudeDegrees'].to_numpy()
Latitude_displ = np.round(Latitude, 3)
Longitude_displ = np.round(Longitude, 3)

#plt.plot(Longitude, Latitude)
#plt.title('Map of Activity')
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
# plt.show()

# --------- Multiplot ---------------------
plt.close('all')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize= (12, 7))
fig.suptitle('Activity Analysis')
ax1.plot(Longitude, Latitude)
ax1.set_xticks(np.round(np.linspace(np.min(Longitude), np.max(Longitude), 5), 3))
ax1.set_title('Map of Activity')
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')

ax2.plot(Dist, Pace)
ax2.set_title('Pace Over Distance')
ax2.set_xlabel('Distance (miles)')
ax2.set_ylabel('Pace (min/mile)')
ax2.set_ylim(13, 2)

ax3.plot(X_axis, Y_axis)
ax3.set_title('Altitude over Distance')
ax3.set_xlabel('Distance (miles)')
ax3.set_ylabel('Altitude (feet)')
ax3.fill_between(X_axis, Y_axis, np.min(Y_axis), color='green')

ax4.bar(bar_positions, Splits)
ax4.set_xticks(bar_positions, Mile_Markers)
ax4.set_title('Splits')
ax4.set_xlabel('Distance (miles)')
ax4.set_ylabel('Pace (min/mile)')
ax4.bar_label(bars, labels = Splits_displ1)
ax4.set_ylim(0, max(Splits) * 1.2)

fig.subplots_adjust(hspace = 0.4, wspace = 0.3)
plt.show()







