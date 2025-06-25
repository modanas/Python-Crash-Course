# Create a class with class attribute a, create a object from it and set 'a' directly using object.a = 0


class Employee:
 a = 4

anas = Employee()
anas.a = 0

print(anas.a)
print(Employee().a)# Which means class attribute doesn't changed