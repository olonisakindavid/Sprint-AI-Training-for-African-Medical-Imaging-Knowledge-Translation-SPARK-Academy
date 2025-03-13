# Hospital Bed Allocation System
# Filename: hospital_bed.py
# Create a `HospitalBed` class with:
# - `bed_number`
# - `patient_name` (default `None`)
# Implement methods:
# - `assign_bed(patient_name)` → Assigns a patient to the bed.
# - `release_bed()` → Frees up the bed

# hospital_bed.py

class HospitalBed:
    def __init__(self, bed_number):
        self.bed_number = bed_number
        self.patient_name = None  # Default patient_name is None

    def assign_bed(self, patient_name):
        """Assigns a patient to the bed."""
        self.patient_name = patient_name

    def release_bed(self):
        """Frees up the bed by setting patient_name to None."""
        self.patient_name = None