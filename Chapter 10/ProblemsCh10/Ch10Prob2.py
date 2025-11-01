class Calculator:
  
  def __init__(self , n):
    self.n = n    
  
  def square_num(self):
    print(self.n**2)
    
  def cube_num(self):
    print(self.n**3)
    
  def squate_root_num(self):
    print(self.n**0.5)
    
    
result = Calculator(4)
print(result.cube_num() , result.square_num()  , result.squate_root_num())

    
    
  