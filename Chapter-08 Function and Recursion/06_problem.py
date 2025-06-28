#program to convert inches to centimetres

def inch_to_cen(inch) :
 return inch * 2.54

inch = int(input("Enter : "))

print(f"Values in centimetres is : {inch_to_cen(inch)}")