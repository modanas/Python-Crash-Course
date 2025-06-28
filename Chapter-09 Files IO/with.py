# f = open("Myfile.txt")

# print(f.read())
# f.close()

# with statement is the best way to open and close file is the with statement
# The same can be written using with statement

with open("Myfile.txt") as f:
 print(f.read())


# You don't have to explicitly close the file