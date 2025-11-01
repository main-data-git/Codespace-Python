#object oriented programing 

# class  => it is like a blan data sheet on which we can fill various data parameters and make it  a object 


# class Employee:
#   name = "hello"
#   age = 20
#   language = "python"
#   salary = 1200000
  
  
# steel = Employee()
# print( steel.name , steel.age , steel.language , steel.salary)


#class attribute and object attribute 
# attribute of the class is class attribute and attribute of a particular object or only used in object are called object attribute .

# instance attribute is like inserting a attribute in an object 

# they also take priority over assigned Attribute



# self parmeter 

# we can put a function inside a class 

# class employee:
#   salary = 12000000
#   language = "python"
  
#   def getinfo(self):
#     print(f"the language is {self.language} and salary is {self.salary} and the name is {self.name}")
    
# harry = employee()
# harry.name = "Harry" 
    
# harry.getinfo()    
# employee.getinfo(harry)



#static method => for function which do not use the object attributes 


# class employee:
#   salary = 12000000
#   language = "python"
  
#   def getinfo(self):
#     print(f"the language is {self.language} and salary is {self.salary} and the name is {self.name}")
    
#   @staticmethod
#   def greet():
#     print("Good Morning")
    
# harry = employee()
# harry.name = "Harry" 
    
# harry.getinfo()   
# harry.greet() 




#__INIT__() constructor => run as soon as the object is created 



class employee:
  salary = 12000000
  language = "python"
  
  def __init__(self , name , language , salary):
    self.name = name
    self.language = language
    self.salary  = salary
    print(" what are you doing here ")
  
  def getinfo(self):
    print(f"the language is {self.language} and salary is {self.salary} and the name is {self.name}")
    
  @staticmethod
  def greet():
    print("Good Morning")
    
harry = employee("Harry" , "Python" , 1400000)
harry.getinfo()

    







    





