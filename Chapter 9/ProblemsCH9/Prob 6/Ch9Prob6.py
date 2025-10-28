with open("Chapter 9/ProblemsCH9/Prob 6/log_file.txt" , "r") as f:
  text  = f.read()
  text1 = text.lower()
  
if "python" in text1:
  print("Python is Present")
else :
  print("Python is Absent")
  
  