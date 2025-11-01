class Programmer:
  company = "Microsoft"
  
  def __init__(self, salary, name , pin , office):
    self.name = name
    self.salary = salary 
    self.pin = pin
    self.office = office
    


p = Programmer(1300000 , "Max" , "Banglore" , "2nd floor")

print(p.name , p.salary , p.pin , p.company , p.office)
    


r = Programmer(1600000 , "Ravi" , "Pune" , "4th floor")

print(r.name , r.salary , r.pin , r.company , r.office)