a = (1,)
print(type(a))

#Methods of tuple

#index method will return the first occurence of the element

my_tuple = (1, 2, 45, 67, 89, 2)
print(my_tuple.index(67)) 

#count method will return the count of the element

print(my_tuple.count(2))

#concatenation of tuple

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenate = tuple1 + tuple2
print(concatenate)

#repetation of tuple

repeated_tuple = tuple1 * 3
print(repeated_tuple)

#membership test

my_tuple = (1, 2, 3, 4, 5)
print(8 in my_tuple)

#unpacking in tuple

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a, b, c)

