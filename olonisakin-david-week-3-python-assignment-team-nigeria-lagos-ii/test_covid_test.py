import pytest
from covid_test import CovidTest


def test_covid_test():
    test = CovidTest("Emma", "2025-03-01")
    assert test.result == "Pending"
    
    test.update_result("Positive")
    assert test.result == "Positive"