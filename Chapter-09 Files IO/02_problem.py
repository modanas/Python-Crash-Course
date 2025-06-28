import random

def game() :
 print("You are playing the game....")
 score = random.randint(1, 61)

 #fetch the hiscore
 with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\hiscore.txt") as f :
  hiscore = f.read()

 if(hiscore != "") :
  hiscore = int(hiscore)
 else :
  hiscore = 0

 print(f"You score : {score} ")
 f
 if(score > hiscore or hiscore=="") :
  #write this hiscore to the file
   with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\hiscore.txt", "w") as f:
    f.write(str(score)) # write takes string as an argument

 return score

game()