

from random import randint

class Train:
  
  
  def __init__(self , trainNo):
    self.trainNo = trainNo
    
  def book(self , fro , to ):
    print(f"Ticket is booked in Train {self.trainNo} from {fro} to {to}")
  
  
  def getStatus(self ):
    print(f"Train no  {self.trainNo} is running on time ")
    
  
  def getFare(self , fro , to ):
    print(f"Ticket fare for  Train {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")
    
    
a = Train(56438)

print( a.book("Delhi" , "Pune") , a.getStatus() , a.getFare("Delhi" , "Pune"))
    
    
    

    

  
  