import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])

youStr = input("Enter your choice : ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
you = youDict[youStr]

# By now we have 2 numbers, one for computer and one for you

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you) :
 print("Draw")

else : 
 if(computer == -1 and you == 1) :
  print("You won") 

 elif(computer == -1 and you == 0) :
  print("You lost")

 elif(computer == 1 and you == -1) :
  print("You Lost")

 elif(computer == 1 and you == 0) :
  print("You won")

 elif(computer == 0 and you == 1) :
  print("You Lost")

 elif(computer == 0 and you == -1) :
  print("You won")

 else :
  print("Something went wrong!")

