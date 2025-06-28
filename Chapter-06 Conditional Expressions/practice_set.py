#program to find greatest of 4 number entered by user
 
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
n3 = int(input("Enter number 3 : "))
n4 = int(input("Enter number 4 : "))

if(n1 > n2 and n1 > n3 and n1 > n4) :
 print("Number 1 is greatest", n1)

elif(n2 > n1 and n2 > n3 and n2 > n4) :
 print("Number 2 is greatest", n2)

elif(n3 > n1 and n3 > n2 and n3 > n4) :
 print("Number 3 is greatest", n3)

else:
 print("Number 4 is greatest", n4)


#qns 2 student has passed if it requires 40% in total and atleast 33% to pass in each subject. Assume 3 subjects 
#and take marks as input

marks1 = int(input("Enter marks of subject 1 : "))
marks2 = int(input("Enter marks of subject 2 : "))
marks3 = int(input("Enter marks of subject 3 : "))

total_percentage = ((marks1 + marks2 + marks3) / 3)

if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33) :
 print("Student is passed")

else:
 print("Student is not passed")

#qsn3 program to detect spam messages

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter message : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)) :
 print("This is spam message")

else:
 print("This is not spam message")

#qsn4 program to check messsage has less than 10 characters

username = input("Enter message : ")
length = len(username)

if(length < 10) :
 print("Message is less than 10 characters")

else:
 print("Message is more than 10 characters")

#qsn5 program to check if name is in the list

name = ["Anas", "Sana", "Rubab", "Zafar"]

username = input("Enter name : ")

if(username in name) :
 print("Name is in the list")

else:
 print("Name is not in the list")

#qsn6 program to find grade of a student

marks = int(input("enter marks : "))

if(marks >= 90 and marks <= 100) :
 grade = "Excellent"

elif(marks >= 80 and marks <= 90 ) :
 grade = "A"

elif(marks >= 70 and marks <= 80) :
 grade = "B"

elif(marks >= 60 and marks <= 70) :
 grade = "C"

elif(marks >= 50 and marks <= 60) :
 grade = "D"

elif(marks < 50) :
 grade = "F"

print("Your grade is : ", grade)

#qsn7 is this post talking about me

post = input("Enter post : ")

if("Anas".lower in post.lower()) :
 print("This post is talking about me")

else:
 print("This post is not talking about me")