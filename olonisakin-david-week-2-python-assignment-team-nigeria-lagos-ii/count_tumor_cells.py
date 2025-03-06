# Count Tumor Cells in an Image (Nested Loops)
# Filename: count_tumor_cells.py
# Write a function `count_tumor_cells(image_matrix)` that scans a 2D NumPy array of an MRI scan,
# counting all nonzero pixels, which represent tumor cells.

import numpy as np
def count_tumor_cells(image_matrix):
    return np.count_nonzero(image_matrix)
