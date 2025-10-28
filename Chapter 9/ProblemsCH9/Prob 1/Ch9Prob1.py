
f = open("poems.txt")
text = f.read()

if "twinkle" in text.lower():
  print("Twinkle is present in the file.")
else:
  print("The word Twinkle is not present in the file")
  
f.close()

