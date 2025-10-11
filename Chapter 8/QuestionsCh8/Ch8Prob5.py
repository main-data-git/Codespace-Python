


# def star_pat(n):
#   for i in range(n):
#     print("*"*(n-i))


def pattern(a):
  if a == 0:
    return "*"
  print("*"*a)
  pattern(a-1)
    
num_row = int(input("Enter the number of rows =>"))
# star_pat(num_row)
pattern(num_row)



  
  
  
  
  
  
  
  