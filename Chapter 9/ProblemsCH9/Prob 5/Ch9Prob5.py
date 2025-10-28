


with open("Chapter 9/ProblemsCH9/Prob 5/random_words_file.txt" , "r" ) as f : # open the file to read  
  text = f.read()
  text1 = text.lower()  #convert the text into lower case
  
num_words = int(input("Enter the number of words you want to replace => ")) #takes the input from to user of the word to be replaced 

for word in range(num_words):                           #runs the loop for the total no of word given to de replaced 
  word = input("Enter the word to be repaced => ")   #takes the replacing  word from the user 
  text1 = text1.replace(word , "#"*len(word))  #replaces the word from the file 




# list_words = ["sun" , "day" , "light" , "time" , "dream"]

# with open("Chapter 9/ProblemsCH9/Prob 5/random_words_file.txt" , "r" ) as f : # open the file to read  
#   text = f.read()
#   text1 = text.lower()  #convert the text into lower case

# for word in list_words:                                    #runs the loop for the total no of word given to de replaced 
#   # ask_word = input("Enter the word to be repaced => ")   #takes the replacing  word from the user 
#   text1 = text1.replace(word , "#"*len(word))              #replaces the word from the file 





with open("Chapter 9/ProblemsCH9/Prob 5/random_words_file.txt" , "w" ) as f:  #open the file again to write 
  f.write(text1)                                                              # writes the file again after replacing 
