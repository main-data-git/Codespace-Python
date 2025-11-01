#inheritance


class Employee:
  company = "ITC"
  name = "ravi"
  salary = 1275563
  
  def show(self):
    print(f"the name is {self.name} and the salary is {self.salary}")
    
    
# class Programmer:
#   company = "ITC infotech"
  
#   def show(self):
#      print(f"the name is {self.name} and the salary is {self.salary}")
     
#   def showLanguage(self):
#     print(f"the name is {self.name} and he is good at {self.language} language")
    
class Programmer(Employee):
  company = "ITC Infotech"
  
  def showLanguage(self):
    print(f"the name is {self.name} and he is good at {self.language}")
  
    
a = Employee()
b = Programmer()

print(a.company)
print(b.company)

b.show()



