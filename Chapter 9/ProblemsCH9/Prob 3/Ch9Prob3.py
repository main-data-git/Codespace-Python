def Table_generator():
  for i in range(2,21):
    file_name = "table" + str(i)
    name = file_name + ".txt"
    # print(name)
    with open(f"Chapter 9/ProblemsCH9/Prob 3/Tables/{name}", 'w') as f:
      f.write(f"This is the table of {i} : \n")
      for j in range(1,11):
        table = f"{i} x {j} = {i*j} \n"
        f.write(table)
        
        
Table_generator()
        
        
        
        
#file_name = "table" + "1"       
#with open(f"{file_name}.txt", 'w') as f:
 # table = f"{3} x {6} = {3*6}"
 # f.write(table)