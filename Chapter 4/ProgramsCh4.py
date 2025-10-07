list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [10, 20, 30, 40, 50]

print(list1[3])
list1[3] = 100
print(list1[3])

print(list2[1:3])

print(list3)

list3.append("hello")
print(list3)


#lista are mutable which means they can be changed 


#append means to add in the last 

li2 = [37,34,567,23,78,786]

li2.sort()
# print(li2)


# li2.reverse()
# print(li2)


li2.insert(2,2222)
print(li2)


li2.pop()
print(li2)

li2.remove(34)
print(li2)




#tuples are immutable which means they cannot be changed
tup1 = (1,2,3,4,5)
tup2 = ('a','b','c','d','e')    
tup3 = (10,20,30,40,50)

tup5 = ()
print(type(tup5))

# tup1[1] = 100

tup7 = (2,3,4,6,3,6,3,56,8,3,1,3,3,4,5,67,78,7,53,2,21,2,3,4345,5,6,67,8,9,0,998,8,7,766,545,43,3,1,2,3,4,5,67,8,899,0,897,76,56,5,)
a = tup7.count(3)

print(a)


print(tup7.index(76))




