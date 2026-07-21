
# Scrap paper for individual testing

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

X = np.array([1, 2, 3, 4, 5, 6, 7])
Y = np.array([5, 6, 3, 4, 8, 12, 4])

plt.plot(X, Y)
plt.show()


'''
fold = os.path.dirname(os.path.realpath(__file__)) # File Search and read Test
fname = 'Test_Spreadsheet.xlsx'
path = os.path.join(fold, fname)

Data_read = pd.read_excel(path, engine='openpyxl')
print(Data_read)
'''

