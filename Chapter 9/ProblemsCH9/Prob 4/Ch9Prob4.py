# file_name = "donkey_file.txt"

with open("Chapter 9/ProblemsCH9/Prob 4/Donkey_file.txt" , "r" ) as f :
  text = f.read()
  text1 = text.lower()
  
new_text = text1.replace("donkey" , "#"*6)

with open("Chapter 9/ProblemsCH9/Prob 4/Donkey_file.txt" , "w" ) as f:
  f.write(new_text)
