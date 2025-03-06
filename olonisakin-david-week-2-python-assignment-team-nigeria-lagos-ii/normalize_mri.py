# NumPy: Normalize MRI Pixel Values
# Filename: normalize_mri.py
# Write a function `normalize_mri(image_array)` that normalizes pixel values in an MRI scan using NumPy.

import numpy as np
def normalize_mri(image_array):
    min_val = np.min(image_array)
    max_val = np.max(image_array)

    # Avoid division by zero if all values are the same
    if max_val == min_val:
        return np.zeros_like(image_array)  # Return an array of zeros

    # Normalize using (x - min) / (max - min)
    return (image_array - min_val) / (max_val - min_val)