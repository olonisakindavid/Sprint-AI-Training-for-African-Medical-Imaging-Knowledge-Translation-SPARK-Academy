import pytest
from patient import Patient


def test_patient():
    patient = Patient("John Doe", 45)
    assert patient.name == "John Doe"
    assert patient.age == 45
    assert patient.medical_history == []
    
    patient.add_medical_record("Diabetes Type 2")
    assert "Diabetes Type 2" in patient.medical_history