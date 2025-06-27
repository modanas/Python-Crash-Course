# try except block

try:
  a = int(input("Enter a number : "))
  b = int(input("Enter a number : "))
  print(a / b)

except ZeroDivisionError as u:
  print("Heyyyyy")
  print(u)
  
except Exception as e:
  print(e)

print("End of a program")