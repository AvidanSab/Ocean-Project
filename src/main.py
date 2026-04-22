import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- STEP 1: LOAD THE DATA ---
data = pd.read_csv('tides.csv')
y_data = data['Predicted (ft)'].astype(float).values

# The historic timeline (Stops at 70 hours)
x_hours = np.arange(len(y_data)) / 10

# The FORECAST timeline (Adds 48 hours / 480 points into the future!)
x_forecast = np.arange(len(y_data) + 480) / 10

# --- STEP 2: DRAW THE RAW HISTORIC DATA ---
plt.plot(x_hours, y_data, color='black', label='Historic NOAA Data')

# --- STEP 3: CALCULATE TRANSFORMATIONS ---
max_height = np.max(y_data)
min_height = np.min(y_data)

total_amplitude = (max_height - min_height) / 2
v_shift = (max_height + min_height) / 2

# --- STEP 4: CALCULATE THE TWO WAVES ---
a_moon = total_amplitude * 0.68  
b_moon = (2 * np.pi) / 12.42
h_moon = x_hours[np.argmax(y_data)] 

a_sun = total_amplitude * 0.32   
b_sun = (2 * np.pi) / 12.00
h_sun = h_moon 

# Plug the NEW future timeline (x_forecast) into the math formulas
y_moon = a_moon * np.cos(b_moon * (x_forecast - h_moon))
y_sun = a_sun * np.cos(b_sun * (x_forecast - h_sun))

# Add both waves together, then lift them up to sea level (v_shift)
y_combined = y_moon + y_sun + v_shift

# --- STEP 5: GRAPH THE FORECAST ---

# Draw the invisible forces (stretching into the future)
plt.plot(x_forecast, y_moon + v_shift, color='purple', alpha=0.3, linestyle='--', label='Lunar Wave')
plt.plot(x_forecast, y_sun + v_shift, color='orange', alpha=0.3, linestyle='--', label='Solar Wave')

# Draw the main prediction line!
plt.plot(x_forecast, y_combined, color='blue', linewidth=2, label='Math Model & Forecast')

# Draw the midline (k)
plt.axhline(y=v_shift, color='red', linestyle=':', label='Vertical Shift (k)')

# Draw the "Current Time" barrier
plt.axvline(x=len(y_data)/10, color='green', linestyle='--', linewidth=2, label='Current Time (Start of Forecast)')

# Final formatting
plt.title("Ocean Tides: Historic Data vs. 48-Hour Mathematical Forecast")
plt.xlabel("Time (Hours)")
plt.ylabel("Water Level (ft)")
plt.legend()

plt.show()