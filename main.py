from Hospital_Project import Patient, Doctor

p1 = Patient("Ravi", 45, "Fever", "P001")
d1 = Doctor("Mehta", "Cardiology", "D001")

p1.details()
d1.add_patient(p1)
d1.diagnose(p1, "Flu")
p1.details()
