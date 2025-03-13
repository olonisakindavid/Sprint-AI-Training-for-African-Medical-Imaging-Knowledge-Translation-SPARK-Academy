import pytest
from blood_bank import BloodBank


def test_blood_bank():
    bank = BloodBank("O+", 10)
    assert bank.blood_type == "O+"
    assert bank.units_available == 10
    
    bank.donate_blood(5)
    assert bank.units_available == 15
    
    bank.request_blood(7)
    assert bank.units_available == 8