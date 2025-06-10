#qsn1 list of 7 fruits entered by user
fruits = []

f1 = input("Enter fruit name : ")
fruits.append(f1)

f2 = input("Enter fruit name : ")
fruits.append(f2)

f3 = input("Enter fruit name : ")
fruits.append(f3)

f4 = input("Enter fruit name : ")
fruits.append(f4)

f5 = input("Enter fruit name : ")
fruits.append(f5)

f6 = input("Enter fruit name : ")
fruits.append(f6)

f7 = input("Enter fruit name : ")
fruits.append(f7)

print(fruits)

#qsn 2 marks of 6 students and display them in sorted order
marks = []

m1 = int(input("Enter marks of student 1 : "))
marks.append(m1)

m2 = int(input("Enter marks of student 2 : "))
marks.append(m2)

m3 = int(input("Enter marks of student 3 : "))
marks.append(m3)

m4 = int(input("Enter marks of student 4 : "))
marks.append(m4)

m5 = int(input("Enter marks of student 5 : "))
marks.append(m5)

m6 = int(input("Enter marks of student 6 : "))
marks.append(m6)

print(marks)
marks.sort()
print(marks)


#qsn 3 list of 4 students and find their sum

marks = [45, 76, 87, 100]
print(sum(marks))

#qsns 4 program to find number of zeroes in a tuple

tuple1 = (7, 0, 0, 8, 0, 9)
print(tuple1.count(0))

