import pytest
from vital_signs import VitalSigns


def test_vital_signs():
    vitals = VitalSigns("Ethan", 75, "120/80")
    assert vitals.heart_rate == 75
    
    vitals.update_vitals(48, "130/85")
    assert vitals.heart_rate == 48
    assert vitals.is_critical() is True