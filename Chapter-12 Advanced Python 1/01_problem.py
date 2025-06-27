# program to open three files 1.txt, 2.txt, 3.txt, if any of these files are not

try :
 with open("1.txt", "r") as f:
  print(f.read())
except Exception as e:
 print(e)

try :
 with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-12 Advanced Python 1\\2.txt", "r") as f:
  print(f.read())
except Exception as e:
 print(e)

try :
 with open("3.txt", "r") as f:
  print(f.read())
except Exception as e:
 print(e)


print("Thank You")
