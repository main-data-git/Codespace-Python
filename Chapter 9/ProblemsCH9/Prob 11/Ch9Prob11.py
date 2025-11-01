with open("/workspaces/Codespace-Python/Chapter 9/ProblemsCH9/Prob 11/text_file_1.txt" , "r") as f:
  text = f.read()
  
  
  
  
with open("Chapter 9/ProblemsCH9/Prob 11/text_file_renamed.txt" , "w") as f:
  f.write(text)
  
