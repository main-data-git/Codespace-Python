

from random import randint

class Train:
  
  
  def __init__(slf , trainNo):
    slf.trainNo = trainNo
    
  def book(slf , fro , to ):
    print(f"Ticket is booked in Train {slf.trainNo} from {fro} to {to}")
  
  
  def getStatus(slf ):
    print(f"Train no  {slf.trainNo} is running on time ")
    
  
  def getFare(slf , fro , to ):
    print(f"Ticket fare for  Train {slf.trainNo} from {fro} to {to} is {randint(222, 5555)}")
    
    
a = Train(56438)

a.book("Delhi" , "Pune") 
a.getStatus()
a.getFare("Delhi" , "Pune")
    
    
    

    

