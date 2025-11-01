
from functools import reduce

a = [21,23,34,45,56,45,45,56,56,67,56,45,34,34,45,4556,56,56,45,45,43,3434]


def greater(a , b):
  if a > b:
    return a
  return b

l = reduce(greater , a)


print(l)