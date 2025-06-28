# program to check whether file contain twinkle or not

f = open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\poem.txt")
data = f.read()

if("twinkle" in data) :
 print("Twinkle is present")

else:
 print("Twinkle is not present")

f.close()