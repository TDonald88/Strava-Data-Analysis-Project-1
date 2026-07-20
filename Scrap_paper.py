
# Scrap paper for individual testing

import pandas as pd
import numpy as np
import os

fold = os.path.dirname(os.path.realpath(__file__))
fname = 'Test_Spreadsheet.xlsx'
path = os.path.join(fold, fname)

Data_read = pd.read_excel(path, engine='openpyxl')
print(Data_read)


