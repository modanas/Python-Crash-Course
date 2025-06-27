# map filter and reduce are higher order functions in python that are used to perform operations on iterables 
# map is used to apply a function to each element of an iterable and return a single value 

listt = [1,2,3,4,5]

square = lambda x: x * x
sqList = map(square, listt)
print(list(sqList))

# filter is used to filter out elements of an iterable based on a condition and return a new
# iterable
listt = [1,2,3,4,5]

even = lambda x: x % 2 == 0
evenList = filter(even, listt)
print(list(evenList))

# reduce is used to apply a function to each element of an iterable and return a single value

from functools import reduce

listt = [1,2,3,4,5]
a = lambda x,y: x + y
sum = reduce(a, listt)
print(sum)