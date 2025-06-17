# replace word donkey with #####

word = "Donkey" and "donkey"

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\myFile.txt", "r") as f:
 data = f.read()

data = data.replace(word, "#####")

with open("C:\\Users\\ACER\\Desktop\\Python\\Chapter-9 Files IO\\myFile.txt", "w") as f:
  f.write(data)
