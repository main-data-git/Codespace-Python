from random import randint

guess_num = randint(1,100)

user_choice = input("Do you want to play the game (Y/N) => ")
attempt_count = 0

if user_choice == "Y" or user_choice == "y":
  while True:
    user_input = int(input("Enter your guessed number => "))
    attempt_count += 1
    if guess_num == user_input:
      print("You guessed the correct number")
      break
    elif user_input > 100 :
      print("Enter number in the range of 1 to 100")
    elif user_input < guess_num:
      print("Higher number please")
    elif user_input > guess_num:
      print("Lower number please")
    else :
      print("Some error in the input try again correctly ")
  
  print(f"Congratulations! You guessed the number {guess_num} and it took you {attempt_count} attempts to guess it")   
else:
  print("Have a good day, come again")
      
      

    





