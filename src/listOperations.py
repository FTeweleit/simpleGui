'''
Created on Apr 30, 2018

@author: felix
'''
MIN_LEN = 3
MIN_DIMENSION = 2


def CheckList(listToCheck: list[int]) -> bool:
    for i in listToCheck:
        if i not in range(10):
            return False
    if len(listToCheck) < MIN_LEN:
        return False
    return True


def ConvertToSquareMatrix(intList: list[int]) -> list[list[int]]:
    dimension = MIN_DIMENSION
    while(dimension ** 2 < len(intList)):
        dimension += 1
    
    matrix: list[list[int]] = list()
    for _ in range(dimension):
        row: list[int] = list()
        for _ in range(dimension):
            try:
                row.append(intList.pop(0))
            except IndexError:
                break
        matrix.append(row)
    return matrix


# Todo: remove since its redundant
def GetDimension(matrix: list[list[int]]) -> int:
    return max(len(matrix), max(len(element) for element in matrix))
