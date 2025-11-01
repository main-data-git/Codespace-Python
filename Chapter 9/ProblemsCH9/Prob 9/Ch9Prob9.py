with open("/workspaces/Codespace-Python/Chapter 9/ProblemsCH9/Prob 9/file1.txt" , "r") as f:
  text1 = f.read()
  
with open("/workspaces/Codespace-Python/Chapter 9/ProblemsCH9/Prob 9/file2.txt" , "r") as f:
  text2 = f.read()
  
if text1 == text2:
  print("theas two files are same ")
else :
  print("these two files are not same ")