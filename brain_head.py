#importing dependencies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#reading dataset
df = pd.read_csv("headbrain.csv")

#visualizing data-set
df.head()

#x and y have been sliced from the dataframe and converted from pandas series to numpy array 
x = df['Head Size(cm^3)'].values
y = df['Brain Weight(grams)'].values

type(x)
type(y)

#calculating mean and length of data-set
x_mean = x.mean()

y_mean = y.mean()

length = len(x)

#calculating the co-efficients of the equation, ie. m and c
#y = m*x + c
num = 0
den = 0

for i in range(length):
    num += (x[i] - x_mean) * (y[i] - y_mean)
    
    den += (x[i] - x_mean) ** 2
    
m = num/den

c = y_mean - (m * x_mean)

print(m , c)

#calculating range between which the line is to plotted 
x_max = np.max(x) + 100
x_min = np.min(x) - 100

#creating an array of X and corresponding Y 
X = np.linspace(x_min, x_max, 1000)
Y = (m*X) + c

#plotting the line of best fit
plt.plot(X, Y, color = 'Red', label = 'Line of best fit')

plt.scatter(x, y, color = 'Blue', label = 'Data points')

plt.xlabel('Head Size(cm^3)')

plt.ylabel('Brain Weight(grams)')

plt.legend()

plt.show()

