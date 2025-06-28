def divisibleBy5(num):
 if num % 5 == 0:
  return True
 return False
 
a = [1234, 45, 79, 87, 975]
f = list(filter(divisibleBy5, a))
print(f)