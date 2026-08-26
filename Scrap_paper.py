
# Scrap paper for individual testing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) # speed
B = np.arange(0, 3, 0.2) # dist
print(A)
print(B)

Splits = []

for n in range(int(np.floor(B.min())), int(np.ceil(B.max())) + 1):
    index = np.where((B >= n) & (B < n + 1))[0]
    if len(index) > 0:
        Splits.append(float(A[index].mean()))

print(Splits)

#C = np.mean(A[int(B[2]):5])
#print(np.where(B == 2))

#for i in range(len(B)):
#    if B[i] == np.floor(B[i]) and B[i] != 0:
#        Splits.append(np.mean(A[(int(B[i]-1)):i]))

#print(Splits)

'''
X = np.array([1, 2, 3, 4, 5, 6, 7]) # test plot
Y = np.array([5, 6, 3, 4, 8, 12, 4])

plt.plot(X, Y)
plt.show()
'''

'''
fold = os.path.dirname(os.path.realpath(__file__)) # File Search and read Test
fname = 'Test_Spreadsheet.xlsx'
path = os.path.join(fold, fname)

Data_read = pd.read_excel(path, engine='openpyxl')
print(Data_read)
'''

