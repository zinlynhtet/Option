import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

strike_prices = np.linspace(50, 150, 25) 
time = np.linspace(0.5, 2, 25) 
strike_prices, time = np.meshgrid(strike_prices, time)
# print(strike_prices, time[:])
implied_volatility = (strike_prices - 100)** 2 / (100 * strike_prices)/ time
fig = plt.figure(figsize=(9, 6))
axis = fig.add_subplot(111, projection='3d')
surface = axis.plot_surface(strike_prices, time, implied_volatility,
                            rstride=1, cstride=1, cmap=plt.cm.coolwarm,
                            linewidth=0.5, antialiased=False)


axis.set_xlabel('strike')
axis.set_ylabel('time-to-maturity')
axis.set_zlabel('implied volatility')
fig.colorbar(surface, shrink=0.5, aspect=5)

plt.show()