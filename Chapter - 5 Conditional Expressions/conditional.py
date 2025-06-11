age = int(input("Enter your age : "))

#if - elif - else ladder
if (age >= 18) :
 print("You are eligible to vote")

elif(age < 0) :
 print("You are not yet born")

elif(age == 0) :
 print("0 is not a valid age.")

else:
 print("You are not eligible to vote")

print("End of program")