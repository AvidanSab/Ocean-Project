import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- STEP 1: LOAD THE DATA ---
data = pd.read_csv('tides.csv')
y_data = data['Predicted (ft)'].astype(float).values

# Historic timeline (stops at the end of the data)
x_hours = np.arange(len(y_data)) / 10

# Forecast timeline (adds 48 hours / 480 points into the future)
x_forecast = np.arange(len(y_data) + 480) / 10

# --- STEP 2: CALCULATE GLOBAL TRANSFORMATIONS ---
max_height = np.max(y_data)
min_height = np.min(y_data)

total_amplitude = (max_height - min_height) / 2
v_shift = (max_height + min_height) / 2

# --- STEP 3: CALCULATE THE THREE WAVES ---
a_moon = total_amplitude * 0.55
a_sun = total_amplitude * 0.20 
a_tilt = total_amplitude * 0.25

b_moon = (2 * np.pi) / 12.42
b_sun = (2 * np.pi) / 12.00
b_tilt = (2 * np.pi) / 24.84

h_moon = x_hours[np.argmax(y_data)]
h_sun = h_moon 
h_tilt = h_moon - 4

# Generate the full timeline for all three waves
y_moon = a_moon * np.cos(b_moon * (x_forecast - h_moon))
y_sun = a_sun * np.cos(b_sun * (x_forecast - h_sun))
y_tilt = a_tilt * np.cos(b_tilt * (x_forecast - h_tilt))

# Superposition (Combine them all)
y_combined = y_moon + y_sun + y_tilt + v_shift

# --- STEP 4: CALCULATE R-SQUARED (Historical Data Only) ---
# Slice the combined line to only look at the historical timeframe
y_model_historic = y_combined[:len(y_data)]

# The actual R^2 Mathematics (Sum of Squares)
ss_res = np.sum((y_data - y_model_historic) ** 2)       # Residual error
ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)        # Total variance
r_squared = 1 - (ss_res / ss_tot)

# --- STEP 5: PRINT THE EQUATION PARAMETERS FOR THE PRESENTATION ---
print("\n" + "="*40)
print("🌊 OCEAN TIDES MODEL PARAMETERS 🌊")
print("="*40)
print(f"Overall Model Accuracy (R²): {r_squared:.4f} ({(r_squared*100):.1f}% accurate)")
print(f"Vertical Shift (k): {v_shift:.3f} ft")
print(f"Total Amplitude:    {total_amplitude:.3f} ft")

print("\n--- 1. LUNAR WAVE (Moon) ---")
print(f"Amplitude (a):   {a_moon:.3f}")
print(f"Period (hours):  12.42")
print(f"Period factor (b): {b_moon:.4f}")
print(f"Phase Shift (h): {h_moon:.2f}")

print("\n--- 2. SOLAR WAVE (Sun) ---")
print(f"Amplitude (a):   {a_sun:.3f}")
print(f"Period (hours):  12.00")
print(f"Period factor (b): {b_sun:.4f}")
print(f"Phase Shift (h): {h_sun:.2f}")

print("\n--- 3. EARTH'S TILT (Diurnal) ---")
print(f"Amplitude (a):   {a_tilt:.3f}")
print(f"Period (hours):  24.84")
print(f"Period factor (b): {b_tilt:.4f}")
print(f"Phase Shift (h): {h_tilt:.2f}")
print("="*40 + "\n")

# --- STEP 6: DRAW THE GRAPH ---
plt.figure(figsize=(12, 6))

# Plot historic raw data
plt.scatter(x_hours, y_data, color='black', label='Historic NOAA Data', s=3, zorder=5)

# Plot the mathematical forecast
plt.plot(x_forecast, y_combined, color='blue', linewidth=2, label='3-Wave Math Model & Forecast', zorder=4)

# Draw the lines
plt.axhline(y=v_shift, color='red', linestyle=':', label='Vertical Shift (k)')
plt.axvline(x=len(y_data)/10, color='green', linestyle='--', linewidth=2, label='Current Time (Forecast Starts)')

# I added the R^2 value directly into the title of the graph!
plt.title(f"Ocean Tides: Real Data vs. 3-Wave Mathematical Forecast (R² = {r_squared:.3f})")
plt.xlabel("Time (Hours)")
plt.ylabel("Water Level (ft)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()