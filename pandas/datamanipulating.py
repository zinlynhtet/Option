import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-darkgrid')

import warnings
warnings.filterwarnings('ignore')

infy = pd.read_csv('data_modules/infy.csv',index_col=['Date'],parse_dates=['Date'],)
print(infy.shape)
print(infy.loc[:,'Close Price'].head())
print(infy.count())

plt.figure(figsize=(9,6))
plt.ylabel('Daily Returns')
# infy['Close Price'].pct_change().plot()
infy['Close Price'].rolling(window=20).mean().plot()
infy['Close Price'].plot()
plt.show()
