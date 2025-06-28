#qsn1 program to create dictionary which take hindi words and with values of thier english translation

words = {
 "madad" : "Help",
 "shukriya" : "Thanks",
 "sukoon" : "Peace",
 "Chota" : "Small",
}

# word = input("Enter the words you want meaning of : ")
# print(words[word])

#qsn2 proram to take 8 values and print their unique value

# s = set() #empty set

# n = input("Enter numbers :")
# s.add(int(n))

# n = input("Enter numbers :")
# s.add(int(n))

# n = input("Enter numbers :")
# s.add(int(n))

# n = input("Enter numbers :")
# s.add(int(n))

# n = input("Enter numbers :")
# s.add(int(n))

# n = input("Enter numbers :")
# s.add(int(n))

# n = input("Enter numbers :")
# s.add(int(n))

# n = input("Enter numbers :")
# s.add(int(n))

# print(s)

#qsn 3 taking 4 friends with their name and faviurite programming language

d = {}

name = input("Enter your name : ")
lang = input("Enter your favourite programming language : ")
d.update({name : lang})

name = input("Enter your name : ")
lang = input("Enter your favourite programming language : ")
d.update({name : lang})

name = input("Enter your name : ")
lang = input("Enter your favourite programming language : ")
d.update({name : lang})

name = input("Enter your name : ")
lang = input("Enter your favourite programming language : ")
d.update({name : lang})

print(d)