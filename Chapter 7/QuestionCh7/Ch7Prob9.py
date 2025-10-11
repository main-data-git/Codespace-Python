n = int(input("Enter the weidth of the ring"))



for i in range(n+1):
  if i == 0 or i == n:
    print("*"*n,end="")
  else:
    print("*" ,end="")
    print(" "*(n-2) ,end="")
    print("*" ,end="")
  print("")


# not completely solved by me 



    
    