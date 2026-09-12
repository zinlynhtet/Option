import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-darkgrid')
import warnings 
warnings.filterwarnings('ignore')

data = pd.read_csv('data_modules/apple_stock_data.csv',index_col=['Date'],parse_dates=['Date'],)
print(data.head())
data['Log_Returns'] = np.log(data['Adj_Close']/data['Adj_Close'].shift(1))
data['20 day Historical Volatility'] = 100*data['Log_Returns'].rolling(window=20).std() * np.sqrt(20)

plt.figure(figsize=(10,7))
plt.plot(data['20 day Historical Volatility'], color = 'b')
plt.xlabel('Date', fontsize = 12)
plt.ylabel('Volatility',fontsize = 12)
plt.title('20 day Historical Volatility',fontsize = 14)
plt.show()