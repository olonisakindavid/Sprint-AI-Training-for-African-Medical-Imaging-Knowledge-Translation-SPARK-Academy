# Vital Signs Monitoring System
# Filename: vital_signs.py
# Create a `VitalSigns` class with:
# - `patient_name`
# - `heart_rate`
# - `blood_pressure`
# Implement methods:
# - `update_vitals(hr, bp)` → Updates heart rate and blood pressure.
# - `is_critical()` → Returns `True` if heart rate < 50 or > 120, or blood pressure is too high/low.
# vital_signs.py

class VitalSigns:
    def __init__(self, patient_name, heart_rate, blood_pressure):
        self.patient_name = patient_name
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure

    def update_vitals(self, hr, bp):
        """Updates the heart rate and blood pressure."""
        self.heart_rate = hr
        self.blood_pressure = bp

    def is_critical(self):
        """Returns True if heart rate < 50 or > 120, or blood pressure is too high/low."""
        systolic, diastolic = map(int, self.blood_pressure.split('/'))
        
        # Check if heart rate is critical
        hr_critical = self.heart_rate < 50 or self.heart_rate > 120
        
        # Check if blood pressure is critical
        bp_critical = systolic > 140 or diastolic > 90 or systolic < 90 or diastolic < 60
        
        return hr_critical or bp_critical