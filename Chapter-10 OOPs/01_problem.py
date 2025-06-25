# Creating a class Programmer for storing informations of few programmers working at microsoft

class Programmer:
   company = "Microsoft"
   def __init__(self, name, salary, pincode):
    self.name = name
    self.salary = salary
    self.pincode = pincode
    
p = Programmer("Anas", "450000", 23)
print(p.company, p.name, p.salary, p.pincode)

  
