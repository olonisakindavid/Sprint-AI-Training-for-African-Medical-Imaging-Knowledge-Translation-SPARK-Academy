# Organ Transplant Waiting List
# Filename: transplant_waitlist.py
# Create a `TransplantWaitingList` class with:
# - `organ` (e.g., kidney, liver)
# - `patients` (list of names)
# Implement methods:
# - `add_patient(name)` → Adds a patient to the waiting list.
# - `remove_patient(name)` → Removes a patient when they receive a transplant.
# transplant_waitlist.py

class TransplantWaitingList:
    def __init__(self, organ):
        self.organ = organ
        self.patients = []  # Initialize an empty list for patients

    def add_patient(self, name):
        """Adds a patient to the waiting list."""
        self.patients.append(name)

    def remove_patient(self, name):
        """Removes a patient from the waiting list when they receive a transplant."""
        if name in self.patients:
            self.patients.remove(name)
        else:
            raise ValueError(f"Patient '{name}' not found in the waiting list.")