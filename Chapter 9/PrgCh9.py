# 
# f = open("textFile.txt")
# 
# data = f.read()
# print(data)
# 
# f.close()
# 
# 



# writing a file 


# st = "Hey harry you are an amazing fellow and a good teacher and a good mentor"

# f = open("textfile.txt" , 'w')

# f.write(st)

# f.close()
  

#More file functions 


f = open("textfile.txt")

# lines = f.readlines()
# print(lines, type(lines))
# f.close()

# line1 = f.readline()
# print(line1 , type(line1))


# line2 = f.readline()
# print(line2 , type(line2))


# line3 = f.readline()
# print(line3 , type(line3))


# line4 = f.readline()
# print(line4 , type(line4))


# line5 = f.readline()
# print(line5 , type(line5))


# line6 = f.readline()
# print(line6 , type(line6))


# line7 = f.readline()
# print(line7 , type(line7))


# line = f.readline()
# while (line != ""):
#     print(line, type(line))
#     line = f.readline()
    
    
# f.close()

                                        
#Apppend in the file using the append function 

# st = " hello world what is the meaning of this fk up statement and the other files are fucked "

# f = open("textfile.txt" , 'a')

# f.write(st) 
# f.close()

# with statement in python =>



# f = open("textfile.txt")
# print(f.read())
# f.close()


with open("textfile.txt") as f:
  print(f.read())


# you don't have to close the file at the last 

















