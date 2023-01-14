#The input below, asks the user to input a 6 digit number
num = input("Please enter a 6 digit number: ")

#A while loop is intialised, which checks to see if the user entered number is 6 digits long. If it is not, then it will ask the user to input again.
while len(num) != 6:
    print("Number entered was not 6 digits.")
    num = input("Please enter a 6 digit number: ")

#The variable smallestNum is declared and initialised and stores the value num.
smallestNum = num

#A for loop is initialised, that will loop from a range of 0, until the len of num - 2, which will always be 4.
for i in range(0, len(str(num)) - 2):
    #The num.replace below is getting a slice of 3 numbers within the string for each index and replacing it with an empty string and stored in calculation
    #This subsequently removes all other numbers around it.
    calculation = int(num.replace(str(num)[i:i+3], ''))
    #The if statement below then determines if it is the smallest number.
    #This is useful for multiple iterations as the next number could be smaller than the previuos one.
    if calculation < int(smallestNum):
        #The value of calculation is then stored in smallestNum
        smallestNum = calculation

#The smallest number is then outputted.
print(f"smallest number is {smallestNum}")