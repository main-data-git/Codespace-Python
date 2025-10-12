n = int(input("Enter the number whose table we need to print"))
def num_table(a):
  for i in range(1,11):
    print(f"{n} X {i} => {n*i}")
    
num_table(n)
  