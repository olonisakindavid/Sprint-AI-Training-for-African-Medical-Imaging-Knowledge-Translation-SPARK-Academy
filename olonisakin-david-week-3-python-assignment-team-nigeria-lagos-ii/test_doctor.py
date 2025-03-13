import pytest
from doctor import Doctor


def test_doctor():
    doctor = Doctor("Dr. Smith", "Cardiology")
    assert doctor.name == "Dr. Smith"
    assert doctor.specialization == "Cardiology"
    
    doctor.add_patient("Alice")
    assert "Alice" in doctor.patients