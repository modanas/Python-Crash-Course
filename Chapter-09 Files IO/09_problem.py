# program to find out whether files are identical and matches the content of another file

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\this.txt", "r") as f1 :
 data1 = f1.read()

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\copy.txt", "r") as f2 :
 data2 = f2.read()

if(data1 == data2) :
 print("Files are identical")

else:
 print("Files are not identical")