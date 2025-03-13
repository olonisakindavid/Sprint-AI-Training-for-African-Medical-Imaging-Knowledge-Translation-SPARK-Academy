import pytest
from transplant_waitlist import TransplantWaitingList


def test_transplant_waitlist():
    waitlist = TransplantWaitingList("Kidney")
    assert waitlist.organ == "Kidney"
    
    waitlist.add_patient("Lucas")
    assert "Lucas" in waitlist.patients
    
    waitlist.remove_patient("Lucas")
    assert "Lucas" not in waitlist.patients