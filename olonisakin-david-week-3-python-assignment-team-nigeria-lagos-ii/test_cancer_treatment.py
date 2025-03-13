import pytest
from cancer_treatment import CancerTreatmentPlan


def test_cancer_treatment():
    treatment = CancerTreatmentPlan("Olivia", "Breast Cancer")
    assert treatment.patient_name == "Olivia"
    
    treatment.add_stage("Chemotherapy")
    assert "Chemotherapy" in treatment.treatment_stages