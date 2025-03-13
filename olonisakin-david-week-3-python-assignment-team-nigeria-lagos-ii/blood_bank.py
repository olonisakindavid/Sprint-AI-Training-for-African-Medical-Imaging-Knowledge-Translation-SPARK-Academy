# Blood Bank Management System
# Filename: blood_bank.py
# Create a `BloodBank` class with:
# - `blood_type`
# - `units_available`
# Implement methods:
# - `donate_blood(units)` → Increases the units available.
# - `request_blood(units)` → Decreases units if enough stock exists.

class BloodBank:
    def __init__(self, blood_type, units_available):
        self.blood_type = blood_type
        self.units_available = units_available

    def donate_blood(self, units):
        """Increases the units of blood available."""
        if units > 0:
            self.units_available += units
        else:
            raise ValueError("Units to donate must be a positive number.")

    def request_blood(self, units):
        """Decreases the units of blood available if enough stock exists."""
        if units <= 0:
            raise ValueError("Units to request must be a positive number.")
        if self.units_available >= units:
            self.units_available -= units
        else:
            raise ValueError("Not enough units available.")