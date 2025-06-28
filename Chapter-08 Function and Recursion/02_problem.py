#program to convert celsius to fahrenheit

def celToFah(C) :
 fah = (C * 9/5) + 32
 return fah

C = int(input("Enter temperature in celsius : "))
print(f"Temperature in fahrenheit is : {celToFah(C)}")