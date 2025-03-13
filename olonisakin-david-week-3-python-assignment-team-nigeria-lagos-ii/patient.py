# Patient Record Management
# Filename: patient.py
# Create a `Patient` class with:
# - `name` (string)
# - `age` (integer)
# - `medical_history` (list)
# Implement methods:
# - `add_medical_record(record)` → Adds a new record to `medical_history`.
# - `get_patient_details()` → Returns the patient's name, age, and medical history.

# patient.py

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.medical_history = []  # Initialize an empty list for medical history

    def add_medical_record(self, record):
        """Adds a new medical record to the patient's medical history."""
        self.medical_history.append(record)

    def get_patient_details(self):
        """Returns the patient's name, age, and medical history as a dictionary."""
        return {
            "name": self.name,
            "age": self.age,
            "medical_history": self.medical_history
        }