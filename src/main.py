import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read/visulize the data
data = pd.read_csv('tides.csv')
y_data = data['Predicted (ft)'].astype(float).values
x_hours = np.arange(len(y_data)) / 10

plt.plot(x_hours, y_data, color='black', label='Raw NOAA Data', marker='.', markersize=5)

max_height = np.max(y_data)
min_height = np.min(y_data)

amplitude = (max_height - min_height) / 2
v_shift = (max_height + min_height) / 2


print("Calculated Amplitude (a):", amplitude)
print("Calculated Vertical Shift (k):", v_shift)

#midline
plt.axhline(y=v_shift, color='red', linestyle='--', label='Vertical Shift (k)')
plt.legend()

plt.show()