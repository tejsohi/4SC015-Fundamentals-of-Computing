#The program here is asking the user to enter a string that is no longer than 50 characters
inputString = input("Please enter a string that is up to 50 characters: ")

#A while loop is initiated to check the the string the user entered is no bigger than 50 characters.
#If the string is bigger than 50 characters, then it will ask the user to input again.
while len(inputString) > 50:
    print("String entered was longer than 50 characters.")
    inputString = input("Please enter a string that is up to 50 characters: ")

#The input below asks the user which word/string they wished to be replaced.
wordToBeReplaced = input("Please enter the word you want to be replaced: ")

#The input below asks the user what they want the WordToBeReplaced, to be changed to. 
replacedWith = input("Please enter the string that you want it to be replaced with: ")

#The print statement below prints the output of the new string.
#inputString.replace takes 2 parameters, the string that is going to be replaced and what it is going to be changed to.
#So the new string that is outputted is the inputted string, but with the values of wordToBeReplaced changed to replacedWith
print(inputString.replace(wordToBeReplaced, f" {replacedWith} ")) 