try:
  with open("1.txt" , "r") as f:
    print(f.read())
    
except Exception as e:
  print(e)


try:
  with open("/workspaces/Codespace-Python/Chapter 12/Problems Ch 12/text file for Prob 1/2.txt" , "r") as f:
    print(f.read())
    
except Exception as e:
  print(e)
  


try:
  with open("3.txt" , "r") as f:
    print(f.read())
    
except Exception as e:
  print(e)
  
  
  
print("Thank you for using the program => ")