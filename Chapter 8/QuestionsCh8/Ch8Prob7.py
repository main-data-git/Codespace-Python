list1 = ["Harry", "Ram", "Max", "Samara", "Raviar", "ar"]
print(list1)
def change_list(a,word):
  n = []
  for i in a:
    if not(i == word):
      n.append(i.strip(word))
  return n
  
a = change_list(list1 , "ar")
print("The new list is => ", change_list(list1, "ar"))



#check it oncve more for errors didn't understand properly