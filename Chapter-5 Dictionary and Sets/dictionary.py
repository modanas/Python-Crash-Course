#Dictionary is a collection of key value pairs in python
marks = {
 "Anas" : 90,
 "Ammar" : 80,
 "Ali" : 70
}

print(marks, type(marks))
print(marks["Anas"])

#dict methods

# items : returns a list of key value tuples
print(marks.items())

#keys : returns a list of keys
print(marks.keys())

#values : returns a list of values 
print(marks.values())

#update : updates the dictionary with the key value pairs from another dictionary
marks.update({"Anas" : 99, "Sam" : 100})
print(marks)

#get : returns the value of the key if it is present in the dictionary
print(marks.get("Anas"))

print(marks.get("Anas2")) #prints none
print(marks["Anas2"]) #returns an error