# Print third, fifth and seventh element of a list using enumerate function

list = [12, 23, 34, 45, 56, 67, 78, 89, 90]

for index, val in enumerate(list):
 if index == 2 or index == 4 or index == 6:
  print(val)