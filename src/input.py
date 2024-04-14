'''
Created on Apr 30, 2018

@author: felix
'''
from listOperations import CheckList, ConvertToSquareMatrix


def GetUserInput() -> list[list[int]]:
    print("Please insert a list of integers divided by ',' and press enter to animate them!")
    givenInput = input("Please note, that a list can only include integer values between 0 and 9\n")
    return _ParseAndConvertString(givenInput)


def _ParseAndConvertString(input: str) -> list[list[int]]:
    intList: list[int] = list()
    for element in input.split(','):
        try:
            intList.append(int(element))
        except ValueError:
            continue
    
    if not CheckList(intList):
        print("something was wrong with your input, the script can not continue!\n")

    matrix: list[list[int]] = ConvertToSquareMatrix(intList)
    print(f"Your input converted into a matrix:\n{matrix}")
    return matrix
