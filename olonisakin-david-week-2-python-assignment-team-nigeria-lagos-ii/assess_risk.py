# Determine Patient Risk Level (Control Structures)
# Filename: assess_risk.py
# Write a function `assess_risk(age, bp, cholesterol)` that classifies a patient's cardiovascular risk
# based on their age, blood pressure, and cholesterol levels.

def assess_risk(age, bp, cholesterol):
    # High risk conditions
    if age >= 60 or bp > 140 or cholesterol > 200:
        return "High"
    # Moderate risk conditions
    elif age > 40 or bp > 130 or cholesterol >= 180:
        return "Moderate"
    # Low risk conditions
    else:
        return "Low"