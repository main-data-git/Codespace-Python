num1  = int(input("Enter the number 1 =>"))
num2  = int(input("Enter the number 2 =>"))
num3  = int(input("Enter the number 3 =>"))
 
 
def greatest_num(a,b,c):
  if a > b and a > c:
    return a 
  elif b > a and b > c:
    return b
  else : 
    return c
 
 
result = greatest_num(num1,num2,num3)

print("The greatest number is " , result)
 
 