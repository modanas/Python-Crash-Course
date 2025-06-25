# Class Train which has methods to book a ticket, get status(no of seats) and get fare information of train running
# under Indian railways

from random import randint
class Train :
 
 def __init__(self, trainNo):
  self.trainNo = trainNo

 def book(self, fro, to):
  print(f"Ticket has been booked in train no. : {self.trainNo} from {fro} to {to}")

 def getStatus(self):
  print(f"Train no.{self.trainNo} is running on time")

 def getFare(self, fro, to):
  print(f"Ticket fare in train no. {self.trainNo} from {fro} to {to} is {randint(100, 5000)}")

t = Train(1234)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")
