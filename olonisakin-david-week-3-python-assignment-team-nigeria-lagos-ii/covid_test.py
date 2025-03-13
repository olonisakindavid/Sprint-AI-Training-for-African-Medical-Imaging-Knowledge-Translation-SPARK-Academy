# COVID-19 Test Center Management
# Filename: covid_test.py
# Create a `CovidTest` class with:
# - `patient_name`
# - `test_date`
# - `result` (default `Pending`)
# Implement methods:
# - `update_result(new_result)` → Updates test result (Positive/Negative).
# - `get_test_info()` → Returns patient name, test date, and result.

# covid_test.py

class CovidTest:
    def __init__(self, patient_name, test_date, result="Pending"):
        self.patient_name = patient_name
        self.test_date = test_date
        self.result = result  # Default result is "Pending"

    def update_result(self, new_result):
        """Updates the test result to a new value (e.g., Positive/Negative)."""
        self.result = new_result

    def get_test_info(self):
        """Returns patient name, test date, and result as a dictionary."""
        return {
            "patient_name": self.patient_name,
            "test_date": self.test_date,
            "result": self.result
        }