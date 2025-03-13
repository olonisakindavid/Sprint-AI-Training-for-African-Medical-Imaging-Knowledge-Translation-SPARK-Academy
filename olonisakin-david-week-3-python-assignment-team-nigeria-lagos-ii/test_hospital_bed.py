import pytest
from hospital_bed import HospitalBed


def test_hospital_bed():
    bed = HospitalBed(101)
    assert bed.bed_number == 101
    assert bed.patient_name is None
    
    bed.assign_bed("Michael")
    assert bed.patient_name == "Michael"
    
    bed.release_bed()
    assert bed.patient_name is None