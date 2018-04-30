'''
Created on Apr 30, 2018

@author: felix
'''
from listOperations import listOperations

print("Hello, please insert a list of integers divided by ',' and press enter to animate them! \n")
givenInput = input("Please note, that a list can only include integer values between 0 and 9\n")
givenInput = givenInput.split(",")
integerList = []
for element in givenInput:
    integerList.append(int(element))
if not listOperations.checkList(listOperations, integerList):
    print("something was wrong with your input, the script can not continue!\n")
else:
    print("Your input was: ")
    print(integerList)
    print("\n")
    matrix = listOperations.convertToMatrix(listOperations, integerList)
    print("Your input converted into a matrix:")
    print(matrix)
    print("\n")