p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter message : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)) :
 print("This is spam message")

else:
 print("This is not spam message")
