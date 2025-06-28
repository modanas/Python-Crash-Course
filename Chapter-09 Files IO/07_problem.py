# program to check word python is in which lines

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\log.txt", "r") as f:
 lines = f.readlines()

lineNo  = 1
for line in lines :
 if("python" in line) :
  print(f"Python is present in line no.{lineNo}")
  break
 lineNo += 1

else:
  print("Python is not present")
