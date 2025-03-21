
# Patient class: store patient details, get patients details
# Doctor class : store doctor details, get patients details
# Hospital class:  link patients with doctors, book appointment, display appointments,
# patient's attention based on severity of condition
# doctor's details: name, ID, specialization
# patient details: age, name, ID, vitals
#symptoms = bp, heart rate, glucose level, temperature 


# Lists to store patient,doctor and appointment records
patient_list = []
doctor_list = []
appointment_list = []

# Class to handle patient details
class PatientDetails:
    def __init__(self, name, age, id, vitals):
        self.name = name
        self.age = age
        self.id = id
        self.vitals = vitals

# Store patient details in patient_list
    def store_patient_details(self):
        patient_info = {"Name": self.name, "Age": self.age, "ID": self.id, "Vitals": self.vitals}
        patient_list.append(patient_info)
        return "Patient details stored."

# Display all patient details
    def display_patient_details(self):
        return patient_list

# Class to handle doctor details
class DoctorDetails:
    def __init__(self, doc_name, doc_id, specialisation):
        self.doc_name = doc_name
        self.doc_id = doc_id
        self.specialisation = specialisation

# Store doctor details in doctor_list
    def store_doctor_details(self):
        doctor_info = {"Name": self.doc_name, "ID": self.doc_id, "Specialisation": self.specialisation}
        doctor_list.append(doctor_info)
        return "Doctor details stored."

# Display all doctor details
    def display_doctor_details(self):
        return doctor_list
# Class to handle symptoms, assess health conditions and check severity of condition
class Symptoms:
    def __init__(self,glucose_level,temp,heart_rate,blood_pressure):
        self.glucose_level = glucose_level
        self.temp = temp
        self.hr = heart_rate
        self.bp = blood_pressure

# Check glucose levels
    def check_glucose(self):
        if self.glucose_level > 200:
            return "Diabetes"
        elif 140 <= self.glucose_level <= 199:
            return "Prediabetes"
        else:
            return "Normal"
        
# Check heart rate
    def check_heart_rate(self):
        if self.hr < 50 or self.hr > 120:
            return "Critical Heart Condition" 
        else:
            return "Normal heart rate"
        
# Check temperature
    def check_temperature(self):
        if 35 <= self.temp <= 38:
            return "Normal temperature"
        elif self.temp < 35:
            return "Hypothermia"
        else:
            return "A fever"

# Check blood pressure
# blood pressure = ["systolic", "diastolic"]
    def check_blood_pressure(self):
        if 110<+ self.bp[0] <= 120 and 70 <= self.bp[1] <= 80:
            return "Normal BP"
        if 120< self.bp[0] < 140 and 80 < self.bp[1] < 89:
            return "Elevated BP"
        else:
            return "High"
    
# Assess overall severity based on multiple vitals
    def assess_severity(self):
        severity = 0
        if Symptoms.check_heart_rate != "Normal heart rate":
            severity += 1
        elif Symptoms.check_blood_pressure != "Normal BP":
            severity += 1
        elif Symptoms.check_glucose() != "Normal":
            severity += 1
        elif Symptoms.check_temperature() != "Normal temperature":
            severity +=1
        
        if severity >=3:
            return "\nSeverity : High!! \n Requires immediate attention"
        elif severity ==2:
            return "\nSeverity: Medium \n Requires less attention than a high severity"
        else:
            return "\nSeverity: Low \n Attention is needed, but not urgent"
        

# Main class to handle hospital management system
class Main:
    #collect vitals from user input
    def vitals():
        try: 
            temp = float(input("Temperature (°C) > "))
            g_level = float(input("Glucose Level (mg/dL) > "))
            bp_systol = int(input("Blood Pressure (mmHg) systolic> "))
            bp_diastol = int(input("Blood Pressure (mmHg) diastolic> "))
            bp = [f"{bp_systol}/{bp_diastol}"]
            HR = int(input("Heart Rate (bpm) > "))
            return  temp, g_level, bp, HR
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return Main.vitals()
    
# Collect patient details
    def patient_input():
        name = input("NAME > ")
        age = int(input("AGE > "))
        ID = int(input("ID NUMBER >"))
        vitals = []
        temp,g_level,bp,HR = Main.vitals()
        vital_list = f'Temperature: {temp}°C, Glucose Level: {g_level} mg/dL, BP: {bp} mmHg, HR: {HR} bpm'
        vitals.append(vital_list)
        patient = PatientDetails(name, age, ID, vitals)
        print(patient.store_patient_details())

# Collect doctor details
    def doctor_input():
        docname = input("NAME > ")
        doc_ID = int(input("ID NUMBER > "))
        specialisation = input("SPECIALIZATION > ")
        doctor = DoctorDetails(docname, doc_ID, specialisation)
        print(doctor.store_doctor_details())

# Update patient details
    def update_patient_details():
        ID = int(input("Enter patient ID to update > "))
        for patient in patient_list:
            if patient["ID"] == ID:
                print(f"Current details: {patient}")
                patient["Name"] = input("New Name (leave blank to keep current) > ") or patient["Name"]
                patient["Age"] = int(input("New Age (leave blank to keep current) > ") or patient["Age"])
                temp,g_level,bp,HR = Main.vitals()
                patient["Vitals"] = [f'Temperature: {temp}°C, Glucose Level: {g_level} mg/dL, BP: {bp} mmHg, HR: {HR} bpm']
                print("Details updated.")
                return
        print("Patient not found.")

#View all patients
    def view_patients():
        if patient_list == []:
            print("List is empty \n Click 1 to add patient details")
        else:
            print("\nPatient Records:")
            for i, patient in enumerate(patient_list,1):
                print(f"{i}. Patient{i}: {patient}")
            
# View all doctors
    def view_doctors():
        if doctor_list == []:
            print(" List is empty \n Click 2 to add Doctor's details")
        else:
            print("\nDoctor Records:")
            for i, doctor in enumerate(doctor_list,1):
                print(f"{i}. Doc{i}:{doctor}")

# Get vital details from a patient
    def get_patient_vitals():
        for patient in patient_list:
            vitals = patient["Vitals"][0]
            print(vitals)
            if vitals is not None:
                temp = float(vitals.split("Temperature: ")[1].split("°C")[0])
                glucose = float(vitals.split("Glucose Level: ")[1].split(" mg/dL")[0])
                bp = vitals.split("BP: ")[1].split(" mmHg")[0].split("/")
                systolic = int(bp[0].split("'")[1])
                diastolic = int(bp[1].split("'")[0])
                bp = [systolic,diastolic]
                hr = int(vitals.split("HR: ")[1].split(" bpm")[0])
                symptoms = Symptoms(glucose,temp,hr,bp)
                print(f'\nPatient ID: {patient["ID"]}')
                print(f"Glucose: {symptoms.check_glucose()}")
                print(f"Temperature: {symptoms.check_temperature()}")
                print(f"Heart Rate: {symptoms.check_heart_rate()}")
                print(f"Blood Pressure: {symptoms.check_blood_pressure()}")
                severity = symptoms.assess_severity()
                print(severity)
            else:
                print("No vitals available for this patient.")

# Booking an appointment
    def book_appointment(patient_id):
        for patient in patient_list:
            if patient["ID"] == patient_id:
                if doctor_list:
                    doctor = doctor_list.pop(0)
                    appointment = {"Patient ID": patient_id, "Doctor": doctor}
                    appointment_list.append(appointment)
                    return f"{patient['Name']} has been assigned to Doctor {doctor['Name']}."
                else:
                    return "No Doctor Assigned."
        return "Patient not found."

#Viewing booked appointment
    def view_appointments():
        if not appointment_list:
            print("No appointments booked.")
        else:
            print("\nAppointments:")
            for app in appointment_list:
                print(app)



# Running the Hospital Management System
while True:
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Update Patient")
    print("4. View Patients")
    print("5. View Doctors")
    print("6. Access Patients Vitals")
    print("7. Book appointment")
    print("8. View Appointment")
    print("9. Exit")

    choice = input("Select an option: ")
    if choice == "1":
        Main.patient_input()
    elif choice == "2":
        Main.doctor_input()
    elif choice == "3":
        Main.update_patient_details()
    elif choice == "4":
        Main.view_patients()
    elif choice == "5":
        Main.view_doctors()
    elif choice == "6":
        Main.get_patient_vitals()
    elif choice == "7":
        patient_id = int(input("Patient ID?"))
        Main.book_appointment(patient_id)
    elif choice == "8":
        Main.view_appointments()
    elif choice == "9":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")