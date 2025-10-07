user_name = input("Enter Username: ")

if len(user_name) < 10:
    print("Username is valid and have less than 10 characters ")
else:
    print("Username is not valid and have more than 10 characters ")