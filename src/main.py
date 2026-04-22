import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read/visulize the data
data = pd.read_csv('tides.csv')
y_data = data['Predicted (ft)'].astype(float).values
x_hours = np.arange(len(y_data))/10

plt.plot(x_hours, y_data, color='black', label='Raw NOAA Data', marker='.', markersize=5)

max_height = np.max(y_data)
min_height = np.min(y_data)

amplitude = (max_height - min_height) / 2
v_shift = (max_height + min_height) / 2

period = (2*3.14)/12.4
total_amplitude = (max_height - min_height) / 2


# --- THE TWO WAVES (SUPERPOSITION) ---

# Wave 1: The Lunar Pull (Stronger, 12.42 hours)
a_moon = total_amplitude * 0.68  
b_moon = (2 * np.pi) / 12.42
h_moon = x_hours[np.argmax(y_data)] # Sync to the highest peak

# Wave 2: The Solar Pull (Weaker, 12.00 hours)
a_sun = total_amplitude * 0.32   
b_sun = (2 * np.pi) / 12.00
h_sun = h_moon 

# Generate the two separate wave formulas
y_moon = a_moon * np.cos(b_moon * (x_hours - h_moon))
y_sun = a_sun * np.cos(b_sun * (x_hours - h_sun))

# Add both waves together, then lift them up to sea level (v_shift)
y_combined = y_moon + y_sun + v_shift


# --- DRAW EVERYTHING ---

# 1. Draw the Moon Wave (in purple, dashed, shifted up to sea level so we can see it)
plt.plot(x_hours, y_moon + v_shift, color='purple', alpha=0.5, linestyle='--', label='Lunar Wave Only')

# 2. Draw the Sun Wave (in orange, dashed, shifted up to sea level)
plt.plot(x_hours, y_sun + v_shift, color='orange', alpha=0.5, linestyle='--', label='Solar Wave Only')

# 3. Draw the Combined Final Model (thick blue)
plt.plot(x_hours, y_combined, color='blue', linewidth=2, label='Combined (Moon + Sun)')

# Midline
plt.axhline(y=v_shift, color='red', linestyle=':', label='Vertical Shift (k)')

plt.legend()
plt.show()