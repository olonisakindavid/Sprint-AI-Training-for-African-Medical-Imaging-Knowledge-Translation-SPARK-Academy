import pytest
from mri_scan import MRI_Scan


def test_mri_scan():
    scan = MRI_Scan("Daniel", "2025-03-01")
    assert scan.patient_name == "Daniel"
    
    scan.add_findings("No abnormalities detected")
    assert scan.findings == "No abnormalities detected"