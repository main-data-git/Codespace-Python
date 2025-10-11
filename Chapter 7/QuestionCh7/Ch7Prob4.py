# To find a number is a prime or not

n = int(input("Enter the number =>"))

for i in range(2,n):
  # print(i)
  if n%i == 0:
    print("It is not a prime number")
    break
  elif i == n-1:
    print("It is a prime number")


