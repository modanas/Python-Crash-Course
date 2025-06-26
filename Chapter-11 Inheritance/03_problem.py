# Create a class Employee and add salary increment properties to it

class Employee:
  salary = 1000
  increment = 500

  @property
  def salaryAfterIncrement(self):
    return self.salary + self.salary * (self.increment/100)
  
  @salaryAfterIncrement.setter
  def salaryAfterIncrement(self, salary):
    self.increment = ((salary / self.salary) - 1) * 100

e = Employee()
# print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 9000
# print(e.salaryAfterIncrement)
print(e.increment)
