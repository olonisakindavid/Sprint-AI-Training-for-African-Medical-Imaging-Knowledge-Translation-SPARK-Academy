# NumPy: Detect Outlier Blood Pressures
# Filename: detect_outliers.py
# Write a function `detect_outliers(bp_array)` that identifies blood pressure outliers
# where values are more than 2 standard deviations away from the mean.

import numpy as np

def detect_outliers(bp_array):
    mean = np.mean(bp_array)  # Calculate the mean
    std_dev = np.std(bp_array)  # Calculate standard deviation

    # Identify values more than 2 standard deviations away from the mean
    outliers = [bp for bp in bp_array if abs(bp - mean) > 2 * std_dev]

    return outliers