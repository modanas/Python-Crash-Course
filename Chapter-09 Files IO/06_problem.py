# program to check whether a log contain word python or not

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\log.txt", "r") as f:
 data = f.read()

 if("python" in data) :
  print("Python is present")

 else:
  print("Python is not present")