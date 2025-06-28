# make a list that contains the multiplication of 7, and program to convert it to vertical strings 
# of same numbers

n = int(input("Enter a number : "))

l = [n * i for i in range(1, 11)]
s = "\n".join([str(i) for i in l])
print(l)