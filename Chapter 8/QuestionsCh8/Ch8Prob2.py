#formula for c to f conversion 
# c/5 = (f - 32)/9


def temp_converter(reading,type):
  if type == 1 :
    result = ((reading - 32)/9)*5
    return result 
  else :
    result = ((reading/5)*9)+32
    return result
  
que_statement = int(input("What are we doing:- \n1. F to C \n2. C to F\n"))
value = int(input("Enter the value"))

result = temp_converter(value,que_statement)

print("The Converted value is = ", result)
  



