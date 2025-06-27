# Program to store the multiplication generated in problem 3 in a file named as Tables.txt

n = int(input("Enter a number : "))

table = [n * i for i in range(1,11)]
with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-12 Advanced Python 1\\tables.txt", "a") as f:
 f.write(f"Table of {n} : {str(table)} \n") #str is used to convert list to string