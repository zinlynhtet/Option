import pandas as pd
import numpy as np

# Ignore warnings
import warnings 
warnings.filterwarnings('ignore')
# my_portfolio = {'Sector': ['IT', 'FMCG', 'Finance', 'Pharma', 'Pharma',
#                            'FMCG', 'FMCG', 'IT', 'Finance', 'Real Estate'],

#                 'Company':   ['Infosys', 'Dabur', 'DHFL', 'Divis Lab', 'Lupin',
#                               'Ruchira Papers', 'Britianna', 'Persistent Systems', 'Bajaj Finance', 'DLF'],

#                 'MarketCap': ['Large Cap', 'Large Cap', 'Mid Cap', 'Mid Cap', 'Mid Cap',
#                               'Small Cap', 'Mid Cap', 'Small Cap', 'Large Cap', 'Mid Cap'],

#                 'Share Price': [1120, 341, 610, 1123, 741, 185, 5351, 720, 1937, 217],

#                 'Amount Invested': [24000, 16000, 50000, 23000, 45000, 12000, 52000, 18000, 5000, 3500]}

# mp = pd.DataFrame(my_portfolio)
# # grouped = mp.groupby(['Sector', 'MarketCap']).groups
# # print(grouped)
# grouped = mp.groupby('MarketCap')
# for name, group in grouped:
#     print(name)
#     print(group)

my_portfolio = {'Sector': ['IT', 'FMCG', 'Finance', 'Pharma', 'Pharma',
                           'FMCG', 'FMCG', 'IT', 'Finance', 'Real Estate'],

                'Company':   ['Infosys', 'Dabur', 'DHFL', 'Divis Lab', 'Lupin',
                              'Ruchira Papers', 'Britianna', 'Persistent Systems', 'Bajaj Finance', 'DLF'],

                'MarketCap': ['Large Cap', 'Large Cap', 'Mid Cap', 'Mid Cap', 'Mid Cap',
                              'Small Cap', 'Mid Cap', 'Small Cap', 'Large Cap', 'Mid Cap'],

                'Share Price': [1120, 341, 610, 1123, 741, 185, 5351, 720, 1937, 217],

                'Amount Invested': [24000, 16000, 50000, 23000, 45000, 12000, 52000, 18000, 5000, 3500]}

mp = pd.DataFrame(my_portfolio)

grouped = mp.groupby('MarketCap')

# print(grouped.get_group('Mid Cap'))
print(grouped['Amount Invested'].agg(np.mean))
print(grouped.agg(np.size))