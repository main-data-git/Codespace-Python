
#WE can also use the recursive methode
'''
sum1 = 1
sum2 = 1 + 2
sum3 = 1 + 2 + 3

suma = sum(a-1) + a
'''
def sum(a):
  if a == 1:
    return 1 
  return sum(a-1) + a

def first_num_sum(a):
  sum = 0 
  i = 1
  while i <= a:
    sum = sum + i
    i += 1
  return sum 



num1 = int(input("Enter the number till where you to print => "))

result1 = first_num_sum(num1)

print(f"The sum of first {num1} natural numbers is => {result1}")
  