def print_scan_timer(scan_time):
    """
    Exercise 17: Use a while loop to simulate an MRI scan timer.
    Print "Scanning... X minutes remaining" until time reaches 0.
    
    Args:
        scan_time (int): Initial scan time in minutes
        
    Returns:
        list: List of status messages generated
    """
    messages = []
    # TODO: Implement while loop to generate timer messages

    while scan_time > 0:
        messages.append(f"Scanning... {scan_time} minutes remaining")
        scan_time -= 1
    
    messages.append("Scan complete!")
    return messages

def find_first_abnormal():
    """
    Exercise 18: Find first SUV value > 3.5 using while loop.
    
    Returns:
        float: First SUV value greater than 3.5
    """
    suv_values = [2.3, 3.2, 4.1, 5.6, 3.0]
    
    # TODO: Implement while loop to find first abnormal value
    i = 0

    while i < len(suv_values):
        if suv_values[i] > 3.5:
            return suv_values[i]
        i += 1
    return None


def reduce_motion_artifacts():
    """
    Exercise 19: Reduce motion_level from 5 to 1, printing each value.
    
    Returns:
        list: List of motion levels during reduction
    """
    motion_level = 5
    levels = []
    
    # TODO: Implement while loop to reduce motion level
    while motion_level >= 1:
        levels.append(motion_level)
        motion_level -= 1
    return levels

def print_patient_info():
    """
    Exercise 20: Use while loop to print patient information key-value pairs.
    
    Returns:
        list: List of formatted strings with patient information
    """
    patient = {
        "ID": 101,
        "Name": "Alice",
        "Age": 45,
        "Modality": "MRI"
    }
    info_strings = []
    
    # TODO: Implement while loop to format patient information
    keys = list(patient.keys()) 
    i = 0
    
    while i < len(keys):
        key = keys[i]
        value = patient[key]
        info_strings.append(f"{key}: {value}")
        i += 1

    return info_strings