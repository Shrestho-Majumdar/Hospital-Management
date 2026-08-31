class Doctor:
    def __init__(self, name, specialization, doctor_id):
        self.name = name
        self.specialization = specialization
        self.doctor_id = doctor_id
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Dr. {self.name} is now treating {patient.name}")

    def diagnose(self, patient, new_disease):
        patient.disease = new_disease
        print(f"Dr. {self.name} diagnosed {patient.name} with {new_disease}")
