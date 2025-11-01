def divisibleBy5(n):
  if n%5 == 0:
    return True
  return False


a = [21,23,34,45,56,45,45,56,56,67,56,45,34,34,45,4556,56,56,45,45,43,3434]

f = list(filter(divisibleBy5, a))

print(f)
