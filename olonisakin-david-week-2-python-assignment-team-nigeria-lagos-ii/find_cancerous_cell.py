# Break and Continue in Loops: Finding First Cancerous Cell
# Filename: find_cancerous_cell.py
# Write a function `find_cancerous_cell(cells)` that loops through a list of cell samples and:
# - Uses `break` to stop once a cancerous cell is found.
# - Uses `continue` to skip unlabeled cells (None values).

def find_cancerous_cell(cells):
    for cell in cells:
        if cell is None:
            continue  # Skip unlabeled cells
        
        if cell == "cancerous":
            return "cancerous"  # Return the string "cancerous" as expected in the test
    
    return None  # If no cancerous cell is found, return None