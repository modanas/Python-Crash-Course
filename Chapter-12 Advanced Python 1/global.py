# global keyword is used to access the global variable in a function

a = 45 # global variable can be used within fncn as well as outside it

def func():
  global a
  a = 3 # local variable
  print(a)

func()
print(a)