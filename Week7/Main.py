from datetime import date

import Patient as pat
# import Practitioner as prt

def main():
    # 1. Take input outside the class
    user_patient_id = input("Enter patient ID: ")
    user_name = input("Enter patient name: ")
    user_dob: date = input("Enter patient DOB: ")
    user_contact_details = input("Enter patient contact details: ")

    # 2. Pass the input into the class constructor
    patient_one = pat.Patient(user_patient_id, user_name, user_dob, user_contact_details)

    print(f"Created: {patient_one.name}, DOB: {patient_one.dob} Contact details: {patient_one.contact_details}")

if __name__ == "__main__":
    main()