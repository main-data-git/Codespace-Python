a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
d = int(input("Enter fourth integer: "))

if a > b and a > c and a > d:
    largest = a
    print("Largest no is :", largest)
elif b > a and b > c and b > d:
    largest = b
    print("Largest no is :", largest)
elif c > a and c > b and c > d:
    largest = c
    print("Largest no is :", largest)
else:
    largest = d
    print("Largest no is :", largest)