# program to make a copy of this.txt

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\this.txt", "r") as f:
 data = f.read()

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\copy.txt", "w") as f:
 f.write(data)