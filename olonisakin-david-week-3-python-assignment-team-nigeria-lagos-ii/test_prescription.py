import pytest
from prescription import Prescription


def test_prescription():
    prescription = Prescription("Sophia")
    assert prescription.patient_name == "Sophia"
    
    prescription.add_medication("Paracetamol", "500mg")
    assert prescription.medications["Paracetamol"] == "500mg"