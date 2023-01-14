#Below, 2 empty lists have been declared and initialised for later use.
listA = []
listB = []

#Here a while loop is initialised to check that the length of listA is not equal to 10, if it is not, then it should continue to ask the user for input 
while len(listA) != 10:
    #The variable listA is used, asking the user for an input. The .splits splits the string every time there is a comma. The [:10] ensures that no more than 10 values are stored in the list
    listA = list(filter(None, input("Please enter a list of 10 numbers seperated by commas: ").split(",")))[:10]

#Here another while loop is initialised to check that the length of listB is also not equal to 10, if it is not, then it should continue to ask the user for input 
while len(listB) != 10:
    #The variable listB is used, asking the user for an input. The .splits splits the string every time there is a comma. The [:10] ensures that no more than 10 values are stored in the list
    listB = list(filter(None, input("Please enter another list of 10 numbers seperated by commas: ").split(",")))[:10]

#The print statement below informs the user to enter a number that will determine if the 2 numbers in the arrays that are at the same index, should be outputted or not.
#The value is then stored in the variable difference.    
print("Please enter the number that will decide if the values in the list should be outputted ")
difference = int(input("This number will determine if the difference between the values is bigger or smaller: "))

#The program is looping through each value in listA. Each individual value is stored as numListA for each loop.
for numListA in listA:
    #The program then loops throuh each value in listB. Each individual value is stored as numListB for each loop.
    for numListB in listB:
        #The program then checks to see if the difference between each value in each list, that are at the same index have a value greater than a number, that has been inputed by the user, shown by the variable difference.
        if int(numListA) - int(numListB) > difference or int(numListB) - int(numListA) > difference:
            #if the statement is true, then the 2 numbers will be outputted like co-ordinates. e.g (10,6) if the difference is greater than 3
            print(f"({numListA}, {numListB})")