class Vector:
  def __init__(self , li):
    self.li = li
    
    # self.x , self.y , self.z = li
    
  # def __add__(self, other):
  #   return Vector(self.x + other.x , self.y + other.y , self.z + other.z)
  
  # def __mul__(self, other):
  #   return Vector(self.x*other.x , self.y*other.y , self.z*other.z)
  
  # def __str__(self):
  #   return f"Vector({self.x} + {self.y} + {self.z}) "
  
  def __len__(self):
    return len(self.li)
  
  
a = Vector([2,3,4])
b = Vector([3,4,6,4,5,6,7,8])

# c = a  + b 
# d = a*b

# print(c)
# print(d) 
print(len(a))
print(len(b))