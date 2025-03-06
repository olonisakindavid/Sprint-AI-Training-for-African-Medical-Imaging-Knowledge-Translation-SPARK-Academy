# Detect COVID Symptoms (Functions & Lists)
# Filename: covid_symptoms_checker.py
# Write a function `covid_symptoms_checker(symptoms)` that checks if a patient has at least
# two of these symptoms: "fever", "cough", "fatigue", "loss of taste", "difficulty breathing".
# Return "Likely COVID" or "Unlikely COVID".

def covid_symptoms_checker(symptoms):
    # List of key COVID symptoms
    covid_symptoms = {"fever", "cough", "fatigue", "loss of taste", "difficulty breathing"}

    # Count how many key symptoms are present in the given list
    count = sum(1 for symptom in symptoms if symptom in covid_symptoms)

    # If at least two key symptoms are found, return "Likely COVID"; otherwise, return "Unlikely COVID"
    return "Likely COVID" if count >= 2 else "Unlikely COVID"
