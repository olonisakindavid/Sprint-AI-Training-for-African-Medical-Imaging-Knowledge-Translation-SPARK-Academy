# Pharmacy Prescription System
# Filename: prescription.py
# Create a `Prescription` class with:
# - `patient_name`
# - `medications` (dictionary with drug names as keys and dosages as values)
# Implement methods:
# - `add_medication(drug, dosage)` → Adds a drug and dosage.
# - `view_prescription()` → Displays all prescribed medications.

# prescription.py

class Prescription:
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.medications = {}  # Initialize an empty dictionary for medications

    def add_medication(self, drug, dosage):
        """Adds a drug and its dosage to the medications dictionary."""
        self.medications[drug] = dosage

    def view_prescription(self):
        """Returns the dictionary of all prescribed medications."""
        return self.medications