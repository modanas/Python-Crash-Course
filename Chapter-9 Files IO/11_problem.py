# program to rename a file to renamed_by_python.txt

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\poem.txt", "r") as f:
 data = f.read()

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\renamed_by_python.txt", "w") as f:
 f.write(data)