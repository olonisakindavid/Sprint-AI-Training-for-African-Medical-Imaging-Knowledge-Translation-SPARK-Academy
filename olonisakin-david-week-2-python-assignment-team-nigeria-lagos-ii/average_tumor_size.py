# Average Tumor Size (Loops & Lists)
# Filename: average_tumor_size.py
# Write a function `average_tumor_size(sizes)` that calculates the average tumor size from a list of measurements.

def average_tumor_size(sizes):
    if not sizes:
        return 0.0
    return sum(sizes) / len(sizes)
    pass  # Implement function