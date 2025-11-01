class Complex:
  def __init__(self , r , i):
    self.r = r
    self.i = i
    
    
  def __add__(self , c2):
    return Complex(self.r + c2.r, self.i + c2.i)
  
  def __mul__(self , c2):
    real_part = self.r*c2.r - self.i*c2.i
    img_part = self.r*c2.i + self.i*c2.r
    return Complex(real_part , img_part)
    
  def __str__(self):
    return f"{self.r} + {self.i}i"
  
    
    
    
    
    
n1 = Complex(1, 2)
n2 = Complex(3, 4)

a = n1 + n2
b = n1*n2

print(a)
print(b)
