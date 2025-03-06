# NumPy: Compute Patient Temperature Stats
# Filename: temperature_stats.py
# Write a function `temperature_stats(temps)` that takes a NumPy array of temperature readings
# and returns the mean, max, and min temperature.

import numpy as np
def temperature_stats(temps):
    mean_temp = np.mean(temps)  # Compute mean
    max_temp = np.max(temps)    # Find max temperature
    min_temp = np.min(temps)    # Find min temperature
    
    return mean_temp, max_temp, min_temp  # Return as a tuple