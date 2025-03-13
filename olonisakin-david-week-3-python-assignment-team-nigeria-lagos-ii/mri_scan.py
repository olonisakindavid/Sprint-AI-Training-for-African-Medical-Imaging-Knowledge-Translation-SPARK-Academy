# Medical Imaging Analysis System
# Filename: mri_scan.py
# Create an `MRI_Scan` class with:
# - `patient_name`
# - `scan_date`
# - `findings` (default `None`)
# Implement methods:
# - `add_findings(report)` → Updates the scan findings.
# - `get_scan_details()` → Returns patient name, date, and findings.

# mri_scan.py

class MRI_Scan:
    def __init__(self, patient_name, scan_date, findings=None):
        self.patient_name = patient_name
        self.scan_date = scan_date
        self.findings = findings  # Default findings is None

    def add_findings(self, report):
        """Updates the scan findings with the provided report."""
        self.findings = report

    def get_scan_details(self):
        """Returns patient name, scan date, and findings as a dictionary."""
        return {
            "patient_name": self.patient_name,
            "scan_date": self.scan_date,
            "findings": self.findings
        }