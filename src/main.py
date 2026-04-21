import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reads/visualized Data
data = pd.read_csv('tides.csv')

y_data = data['Predicted (ft)'].astype(float).values
x_hours = np.arange(len(y_data))/10

plt.plot(x_hours, y_data)
plt.xlabel('Hours')
plt.ylabel('Wave Height')



max_height = np.max(y_data)
min_height = np.min(y_data)

amplitude = (max_height-min_height)/2
v_shift = (max+min)/2

plt.show()