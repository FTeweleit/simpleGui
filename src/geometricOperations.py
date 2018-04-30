'''
Created on Apr 30, 2018

@author: felix
'''
from listOperations import listOperations

class geometryCalc(object):
    '''
    contains the necessary operations to calculate the sizes of rectangles and squares
    '''
    #returns the size of the rectangle x and y border in a list, first entry is x size, second y size
    @staticmethod
    def rectangleSize(self, matrix, xWindowSize, yWindowSize, xBorder, yBorder, innerBorder):
        rectangleAmount = listOperations.getDimension(listOperations,matrix)
            
        #calculate the space for each rectangle if they have a distance in between, called inner border
        xSpace = xWindowSize - 2 * xBorder - (rectangleAmount + 1) * innerBorder
        ySpace = yWindowSize - 2 * yBorder - (rectangleAmount + 1) * innerBorder
            
        xRectangleSize = xSpace // rectangleAmount
        yRectangleSize = ySpace // rectangleAmount
            
        return [xRectangleSize, yRectangleSize] 
    
    #returns a list, containing the center point x and y and the radius of the circle in a list, in this order
    @staticmethod
    def circleSize(self, rectangleSize):
        xRelativeCircleCenter = rectangleSize[0] // 3
        yRelativeCircleCenter = rectangleSize[1] // 3
        if rectangleSize[0] < rectangleSize[1]:
            radius = rectangleSize[0] / 6
        else:
            radius = rectangleSize[1] / 6
        return [xRelativeCircleCenter, yRelativeCircleCenter, radius]