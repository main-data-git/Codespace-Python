#sets and dictonaries 

# dictonary have key value pairs                     


# marks = {
#     "maths": 90,
#     "science": 80,
#     "english": 85
# }


# print(marks,type(marks))

# print(marks["science"])

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"history": 70})
# print(marks)

# print(marks.get("maths"))gives none if not found 
# print(marks["maths"])gives error if not found
# for i in marks:
#   print(i)
#   print(marks[i])
#   print(marks.get("maths"))


# marks.clear()
# print(marks)  


#Sets are unordered collection of unique items  

s1 = {1, 2, 3, 4, 5, 5, 6, 7, 8, 8}
s2 = {5, 6, 7, 8, 9, 10}
# ba =  set()
# ab = {}
# print(type(ab))
# print(type(ba))

# print(s)

# s.add(9)
# s.add(10) 
# print(s)
# s.clear()
# print(s)


# a = {
#   "max": 1,
#   "harry": 2
# }

# b = len(a)
# print(b)
# s.remove("max")
# print(s)


print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))