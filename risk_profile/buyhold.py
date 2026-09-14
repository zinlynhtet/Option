import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

daily_stock_data = pd.read_csv('data_modules/stocks_data_2010_2020.csv', index_col=0)
daily_stock_data.index = pd.to_datetime(daily_stock_data.index)
monthly_stock_data = daily_stock_data.asfreq('Y')
result = monthly_stock_data.dropna()
change = result.pct_change()
r_change = change.dropna()
p_returns= r_change.mean(1)
cum_p_returns = (p_returns +1).cumprod()
plt.style.use('seaborn-v0_8-darkgrid')
cum_p_returns.plot(figsize= (10,7))
plt.title("Buy and Hold Strategy")
plt.xlabel('Date')
plt.ylabel('Cumulative Portfolio Return')
plt.show()