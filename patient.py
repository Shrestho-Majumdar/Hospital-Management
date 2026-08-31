class Patient:
 def __init__(self,name,age,disease,p_id):
    self.name=name
    self.age=age
    self.disease=disease
    self.p_id=p_id
    self.admitted=False
 def admit(self):
    self.admitted=True
    print(f"{self.name}has been admitted")
 def details(self):
    if self.admitted==True:
        print(f"patient name={self.name},age={self.age},disease={self.disease},patient_id={self.p_id}")
    else:
        print("no data")
