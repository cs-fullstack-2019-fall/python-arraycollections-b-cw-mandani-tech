# # python-arrayCollections_b-cw

# Problem 1:
# Create a function with the variable below. After you create the variable do the instructions below that.
# ```
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# ```
# a) Print the 3rd element of the numberList.
# b) Print the size of the array
# c) Delete the second element.
# d) Print the 3rd element.
def teacherNames():
    arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblem2[2])
    lenght=len(arrayForProblem2)
    print(lenght) #prints lenght
    arrayForProblem2.pop(1)  #Delete the second element.
    print(arrayForProblem2[2])
teacherNames()

# Problem 2:
# We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def exitFunc ():
    userInput=0
    while(userInput !='q'):
        userInput=input("Enter a String or q to quit :")
exitFunc()

# Problem 4:
# Create an array of 5 numbers. <strong>Using a loop</strong>, print the elements in the array reverse order.
# <strong>Do not use a function</strong>
numberList =[ 1,2,3,4,5]
lenght= len(numberList) # finding the lenght of the list
for z in range (lenght-1,-1,-1):
      print(numberList[z]) # prints reverse list

# Problem 5:
# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def hardcodedFunc():
    hardcodedList=[12,14,16,3,6,1,0,]
    userInput=int(input("Enter a number: ")) # input from user
    highCount=0
    lowCount=0
    for x in hardcodedList:
        if x>userInput:  # check for higher number
            highCount=highCount+1
        elif x<userInput:  # check for lower number
            lowCount=lowCount+1
        else:
            print(f"{userInput} is a number present in the list")
    print(f'{highCount} higher numbers in list')
    print(f'{lowCount} lower numbers in the list')
def problem5():
    hardcodedFunc()
problem5()