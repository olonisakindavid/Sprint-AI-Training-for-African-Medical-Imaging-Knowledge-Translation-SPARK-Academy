import numpy as np

def find_scan_time_range():
    """
    Exercise 21: Find minimum and maximum scan times.
    
    Returns:
        tuple: (minimum scan time, maximum scan time)
    """
    scan_times = np.array([12.5, 8.0, 15.2, 10.3])
    
    # TODO: Find min and max values
    min_time = np.min(scan_times)
    max_time = np.max(scan_times)
    
    return min_time, max_time


def calculate_mean_suv():
    """
    Exercise 22: Calculate mean SUV value.
    
    Returns:
        float: Mean SUV value
    """
    suv_values = np.array([2.3, 4.1, 1.8, 5.6, 3.9])
    
    # TODO: Calculate mean value
    mean_suv = np.mean(suv_values)
    
    return mean_suv


def normalize_suv_values():
    """
    Exercise 23: Normalize SUV values using (value - min) / (max - min).
    
    Returns:
        numpy.ndarray: Array of normalized SUV values
    """
    suv_values = np.array([2.3, 4.1, 1.8, 5.6, 3.9])
    
    # TODO: Implement normalization
    normalized_suv = (suv_values - np.min(suv_values)) / (np.max(suv_values) - np.min(suv_values))
    
    return normalized_suv


def threshold_scan_times():
    """
    Exercise 24: Create array where values > 10 are "Long", others "Short".
    
    Returns:
        numpy.ndarray: Array of scan time classifications
    """
    scan_times = np.array([12.5, 8.0, 15.2, 10.3])
    
    # TODO: Implement thresholding
    thresholded_times = ["Long" if values > 10 else "Short" for values in scan_times]
    return thresholded_times


def transform_pixel_intensities():
    """
    Exercise 25: Apply log transformation to pixel intensities.
    
    Returns:
        numpy.ndarray: Array of log-transformed intensities
    """
    pixel_intensities = np.array([10, 50, 100, 200])
    
    # TODO: Apply log transformation
    transformed = np.ndarray(pixel_intensities)
    
    return transformed


def count_threshold_pixels():
    """
    Exercise 26: Count pixels with values > 200 in a CT scan.
    
    Returns:
        int: Number of pixels above threshold
    """
    ct_scan = np.array([120, 250, 300, 100])
    
    # TODO: Count pixels above threshold
    count = [values for values in ct_scan if values > 200]
    
    return count
