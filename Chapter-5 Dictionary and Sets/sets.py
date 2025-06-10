#Sets is non-repetitive collection of unique elements in python

my_set  = {1, 2, 3, 4, 4, "Anas", "Sana", "Anas"}
print(my_set, type(my_set))


#Methods of sets
#1. add method will add the element to the set

my_set.add("Yoyo")
print(my_set)

#union method will return the union of two sets

set1 = {1, 45, 6, 78}
set2 = {7, 8, 1, 78}
print(set1 - set2)
print(set1.union(set2))

#intersection method will return the intersection of two sets

print(set1.intersection(set2))

