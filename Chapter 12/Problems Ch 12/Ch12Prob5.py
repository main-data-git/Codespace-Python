n = int(input("Ebter a number => "))




table = [n*i for i in range(1,11)]


with open("/workspaces/Codespace-Python/Chapter 12/Problems Ch 12/tablesfileforprob5.txt" , "a") as f :
  f.write(str(table) + "\n")
  