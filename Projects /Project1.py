#Snake , Water , Gun Game 
#Rock , Paper , Scissor

'''
1 for snake 
-1 for  water 
0 for gun 

random number generator
'''
import random

while True :
  comp_input =  random.randint(-1, 1)
 
  user_input = input("Enter your choice => ")

  ans_dict = { "s":1 , "w":-1 , "g":0 }
  rev_ans_dict = { 1:"Snake" , -1:"Water" , 0:"Gun" }
  your_ans = ans_dict[user_input]

  print(f"Your choice is {rev_ans_dict[your_ans]} \nComputer`s choice is {rev_ans_dict[comp_input]}")

  if comp_input == your_ans:
      print("It`s a Draw!")
  else :
    if comp_input == -1 and your_ans == 1:
      print("You Win!")
    elif comp_input == -1 and your_ans == 0:
      print("You Lose!")
    elif comp_input == 1 and your_ans == 0:
      print("You Win!")
    elif comp_input == 1 and your_ans == -1:
      print("You Lose!")
    elif comp_input == 0 and your_ans == 1:
      print("You Lose!")
    elif comp_input == 0 and your_ans == -1:
      print("You Win!")
    else :
      print("Something went wrong ")  
      
      
#make your own logic or  pattern and short hand the code 

# like comp_input - your_ans = 1 and -2
# if comp_input-your_ans == 1 or comp_input - your_ans == -2:
#   print("You Win!")
# else :
#   print("You Lose!")              