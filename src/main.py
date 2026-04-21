import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('tides.csv')

y_data = data['Predicted (ft)'].astype(float).values
x_hours = np.arange(len(y_data))/10

plt.plot(x_hours, )
