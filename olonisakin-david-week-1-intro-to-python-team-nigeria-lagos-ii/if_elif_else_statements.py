def scan_type_classification():
    """
    Given modality = "MRI", write an if-elif-else statement that prints:
    "Magnetic Resonance Imaging" for "MRI",
    "Computed Tomography" for "CT",
    "Other imaging modality" otherwise.
    
    Returns:
        str: The classification of the imaging modality.
    """
    modality = "MRI"
    if modality == "MRI":
        return "Magnetic Resonance Imaging"
    elif modality == "CT":
        return "Computed Tomography"
    else:
        return "Other imaging modality"

def patient_risk_level():
    """
    Given age = 65, classify the patient’s risk level:
    "High risk" if age > 60,
    "Moderate risk" if 40 ≤ age ≤ 60,
    "Low risk" otherwise.
    
    Returns:
        str: The patient risk classification.
    """
    age = 65
    if age > 60:
        return "High risk"
    elif 40 <= age <= 60:
        return "Moderate risk"
    else:
        return "Low risk"

def image_resolution_classification():
    """
    Given resolution = "512x512", write an if-elif-else statement that classifies it as:
    "Low Resolution" if width < 512,
    "Medium Resolution" for 512 ≤ width ≤ 1024,
    "High Resolution" otherwise.
    
    Returns:
        str: The resolution classification.
    """
    resolution = "512x512" #width x height
    width = int(resolution.split('x')[0])
    if width < 512:
        return "Low Resolution"
    elif 512 <= width <= 1024:
        return "Medium Resolution"
    else:
        return "High Resolution"

def determine_contrast_type():
    """
    Determine Contrast Type for MRI:
    If patient_age < 10, use "Pediatric contrast",
    If 10 ≤ patient_age < 60, use "Standard contrast",
    Otherwise, use "Low-dose contrast".
    
    Returns:
        str: The contrast type.
    """
    patient_age = 55
    if patient_age < 10:
        return "Pediatric contrast"
    elif 10 <= patient_age < 60:
        return "Standard contrast"
    else:
        return "Low-dose contrast"

def scan_time_warning():
    """
    Given scan_time in minutes, print:
    "Fast scan" if time < 10,
    "Optimal scan" if 10 ≤ time ≤ 20,
    "Long scan, check settings" otherwise.
    
    Returns:
        str: The scan time classification.
    """
    scan_time = 20
    if scan_time < 10:
        return "Fast scan"
    elif 10 <= scan_time <= 20:
        return "Optimal scan"
    else:
        return "Long scan, check settings"

def detect_motion_artifacts():
    """
    Given motion_level (ranging from 1 to 5), classify as:
    "Minimal artifact" if motion_level == 1,
    "Moderate artifact" if 2 ≤ motion_level ≤ 3,
    "Severe artifact, re-scan required" otherwise.
    
    Returns:
        str: The motion artifact classification.
    """
    motion_level = 3 
    if motion_level == 1:
        return "Minimal artifact"
    elif 2 <= motion_level <= 3:
        return "Moderate artifact"
    else:
        return "Severe artifact, re-scan required"