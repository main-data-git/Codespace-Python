

with open("/workspaces/Codespace-Python/Chapter 9/ProblemsCH9/Prob 7/log_file_ch7.txt" , "r") as f :
  lines  = f.readlines()
  
  
line_no = 1

for line in lines:
  if "python" in line:
    print(f"Python is Present and the line no is {line_no}")
    break
  line_no += 1   
else :
  print("Python is Absent")
  
  
  
  

  


