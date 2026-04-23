import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('tides.csv')
y_data = data['Predicted (ft)'].astype(float).values
x_hours = np.arange(len(y_data)) / 10

x_forecast = np.arange(len(y_data) + 480) / 10

plt.scatter(x_hours, y_data, color='black', label='Historic NOAA Data', s = 1)

max_height = np.max(y_data)
min_height = np.min(y_data)

total_amplitude = (max_height - min_height) / 2
v_shift = (max_height + min_height) / 2
r_squared =


a_moon = total_amplitude * 0.55
a_sun = total_amplitude * 0.20 
a_tilt = total_amplitude * 0.25

b_moon = (2 * np.pi) / 12.42
b_sun = (2 * np.pi) / 12.00
b_tilt = (2 * np.pi) / 24.84

h_moon = x_hours[np.argmax(y_data)]
h_sun = h_moon 
h_tilt = h_moon - 4

y_moon = a_moon * np.cos(b_moon * (x_forecast - h_moon))
y_sun = a_sun * np.cos(b_sun * (x_forecast - h_sun))
y_tilt = a_tilt * np.cos(b_tilt * (x_forecast - h_tilt))

y_combined = y_moon + y_sun + y_tilt + v_shift


plt.plot(x_forecast, y_combined, color='blue', linewidth=2, label='3-Wave Math Model & Forecast')

plt.axhline(y=v_shift, color='red', linestyle=':', label='Vertical Shift (k)')

plt.axvline(x=len(y_data)/10, color='green', linestyle='--', linewidth=2, label='Current Time (Forecast Starts)')

plt.title("Ocean Tides: Real Data vs. 3-Wave Mathematical Forecast")
plt.xlabel("Time (Hours)")
plt.ylabel("Water Level (ft)")
plt.legend()

plt.show()