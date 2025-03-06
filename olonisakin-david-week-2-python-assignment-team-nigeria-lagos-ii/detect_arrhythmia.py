# Find Abnormal Heart Rates (Loop & Condition)
# Filename: detect_arrhythmia.py
# Write a function `detect_arrhythmia(heart_rates)` that takes a list of heart rate readings
# and returns a list of values above 120 BPM or below 50 BPM.

def detect_arrhythmia(heart_rates):
    # Find abnormal heart rates (above 120 BPM or below 50 BPM)
    return [rate for rate in heart_rates if rate > 120 or rate < 50]