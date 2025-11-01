class Vector:
  def __init__(self , x , y , z):
    self.x = x
    self.y = y
    self.z = z
    
  def __add__(self, other):
    return Vector(self.x + other.x , self.y + other.y , self.z + other.z)
  
  # def __mul__(self, other):
  #   return Vector(self.x*other.x , self.y*other.y , self.z*other.z)
  
  def __str__(self):
    return f"Vector({self.x}i + {self.y}j + {self.z}k) "
  
  
a = Vector(2,3,4)
b = Vector(3,4,6)

c = a  + b 
# d = a*b

print(c)
# print(d) 