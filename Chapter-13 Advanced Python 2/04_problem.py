from functools import reduce

listt = [111, 895, 78, 90, 876, 123]

def greater(a, b):
 if a > b:
  return a
 return b

print(reduce(greater, listt))