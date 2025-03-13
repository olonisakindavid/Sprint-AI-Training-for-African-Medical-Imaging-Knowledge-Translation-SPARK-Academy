# Cancer Treatment Plan Management
# Filename: cancer_treatment.py
# Create a `CancerTreatmentPlan` class with:
# - `patient_name`
# - `cancer_type`
# - `treatment_stages` (list of planned treatments)
# Implement methods:
# - `add_stage(stage)` → Adds a new treatment stage.
# - `get_treatment_plan()` → Returns all planned treatment stages.

class CancerTreatmentPlan:
    def __init__(self, patient_name, cancer_type):
        self.patient_name = patient_name
        self.cancer_type = cancer_type
        self.treatment_stages = []  # Initialize an empty list for treatment stages

    def add_stage(self, stage):
        """Adds a new treatment stage to the plan."""
        self.treatment_stages.append(stage)

    def get_treatment_plan(self):
        """Returns all planned treatment stages."""
        return self.treatment_stages