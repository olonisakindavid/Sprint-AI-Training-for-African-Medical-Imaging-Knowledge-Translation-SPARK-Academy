# Doctor Information System
# Filename: doctor.py
# Create a `Doctor` class with:
# - `name`
# - `specialization`
# - `patients` (list)
# Implement methods:
# - `add_patient(patient_name)` → Adds a patient's name to the list.
# - `list_patients()` → Returns all assigned patients.
# doctor.py

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patients = []  # Initialize an empty list for patients

    def add_patient(self, patient_name):
        """Adds a patient's name to the list of patients."""
        self.patients.append(patient_name)

    def list_patients(self):
        """Returns the list of all assigned patients."""
        return self.patients