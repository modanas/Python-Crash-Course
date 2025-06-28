# repeat program 4 for a list of words

words = ["Donkey", "bad", "ganda", "donkey"]

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\myFile.txt", "r") as f:
 data = f.read()

for word in words :
 data = data.replace(word, "#" * len(word))

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\myFile.txt", "w") as f:
  f.write(data)
