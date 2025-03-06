# Blood Sugar Level Alert (if/elif/else)
# Filename: check_glucose.py
# Write a function `check_glucose(glucose_level)` that evaluates glucose levels and returns:
# - "Diabetes" if glucose_level > 200
# - "Prediabetes" if 140 <= glucose_level <= 199
# - "Normal" otherwise

def check_glucose(glucose_level):
    if glucose_level > 200:
        return "Diabetes"
    elif 140 <= glucose_level <= 199:
        return "Prediabetes"
    else:
        return "Normal" 
    pass  # Implement function