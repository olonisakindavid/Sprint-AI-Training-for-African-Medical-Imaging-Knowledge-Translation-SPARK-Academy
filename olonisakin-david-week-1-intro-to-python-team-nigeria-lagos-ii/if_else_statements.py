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
    age = 40
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
    patient_age = 12
    if patient_age < 10:
        return "Pediatric contrast"
    elif 10 <= patient_age <60:
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
    scan_time = 40
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
    motion_level = 1
    if motion_level == 1:
        return "Minimal artifact"
    elif 2 <= motion_level <= 3:
        return "Moderate artifact"
    else:
        return "Severe artifact, re-scan required" 

def check_scan_time():
    """
    Given scan_time = 12.5 (in minutes), write an if-else statement that prints "Scan completed successfully" 
    if the scan time is less than 15 minutes, otherwise print "Scan took too long".
    
    Returns:
        str: The scan completion status.
    """
    scan_time = 12.5
    if scan_time < 15:
        return "Scan completed successfully"
    else:
        return "Scan took too long"

def contrast_injection_decision():
    """
    A CT scan requires contrast if the patient’s weight is above 70 kg. Write an if-else statement that prints 
    "Inject contrast" if patient_weight > 70, otherwise "No contrast needed".
    
    Returns:
        str: The contrast injection decision.
    """
    patient_weight = 100
    if patient_weight > 70:
        return "Inject contrast"
    else:
        return "No contrast needed"

def abnormal_suv_detection():
    """
    Given a PET scan SUV value suv = 4.2, print "Abnormal" if the SUV value is greater than 3.5, otherwise "Normal".
    
    Returns:
        str: The SUV classification.
    """
    suv = 4.2
    if suv > 3.5:
        return "Abnormal"
    else:
        return "Normal"

def patient_age_validation():
    """
    Given age = 16, write an if-else statement that prints "Eligible for MRI" if the patient is 18 or older, 
    otherwise "MRI not recommended for minors".
    
    Returns:
        str: The MRI eligibility decision.
    """
    age = 16
    if age >= 18:
        return "Eligible for MRI"
    else:
        return "MRI not recommended for minors"

def check_if_grayscale():
    """
    Given channels = 1, write an if-else statement to print "Grayscale Image" if channels == 1, 
    otherwise print "Color Image".
    
    Returns:
        str: The image type classification.
    """
    channels = 1
    if channels == 1:
        return "Grayscale Image"
    else:
        return "Color Image"

def check_scan_urgency():
    """
    If a scan has "high" priority, print "Urgent scan, process immediately", otherwise print 
    "Regular scan, process as scheduled".
    
    Returns:
        str: The scan urgency classification.
    """
    priority = "high"
    if priority.lower() == "high": 
        return "Urgent scan, process immediately"
    else:
        return "Regular scan, process as scheduled"