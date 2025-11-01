class Calculator:
  
  def __init__(self , n):
    self.n = n    
  
  def square_num(self):
    print(self.n**2)
    
  def cube_num(self):
    print(self.n**3)
    
  def squate_root_num(self):
    print(self.n**0.5)
    
  @staticmethod
  def end_note():
    print("Thanks for using")
    
a = Calculator(4)

a.square_num() 
a.end_note()
  