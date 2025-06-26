# Create a class Pet from Animal and further create a class Dog from Class Pet and add a method Bark to the Dog

class Animal:
 def __init__(self):
  self.name = name

class Pet(Animal):
 def __init__(self):
  pass

class Dog(Pet):
 def __init__(self):
  pass

 @staticmethod 
 def bark():
  print("Bark")

d = Dog()
d.bark()