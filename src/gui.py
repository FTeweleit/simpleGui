'''
Created on Apr 30, 2018

@author: felix
'''
from tkinter import *
from geometricOperations import geometryCalc
from input import matrix

toAnimate = matrix

master = Tk()

#numbers here are hard coded, but it can easily be changed into dynamic window sizes etc.
windowHeight = 800
windowWidth = 800
xBorder = 20
yBorder = 20
innerRectangleBorder = 5
drawingDevice = Canvas(master, width = windowWidth, height = windowHeight)
drawingDevice.create_rectangle(0, 0, 800, 800, fill = "#fff")
drawingDevice.pack()

rectangleSize = geometryCalc.rectangleSize(geometryCalc, toAnimate, windowWidth, windowHeight, xBorder, yBorder, innerRectangleBorder)
circleSize = geometryCalc().circleSize(geometryCalc,rectangleSize)

actualRow = 0
actualColumn = 0
for entry in toAnimate:
    for value in entry:
        #calculate the actual points to draw the rectangles and actually draw the rectangle
        xStartPoint = xBorder + actualColumn * rectangleSize[0] + innerRectangleBorder * (actualColumn + 1)
        xEndpoint = xBorder + (actualColumn + 1) * rectangleSize[0] + innerRectangleBorder * (actualColumn + 1)
        
        yStartPoint = yBorder + actualRow * rectangleSize[1] + innerRectangleBorder * (actualRow + 1)
        yEndPoint = yBorder + (actualRow + 1) * rectangleSize[1] + innerRectangleBorder * (actualRow + 1)
        
        drawingDevice.create_rectangle(xStartPoint, yStartPoint, xEndpoint, yEndPoint, outline = "#11eb11")
        
        actualColumn += 1
        #draw the circles in the rectangle
        if value == 0 or value > 9 :
            continue
        j = 0
        k = 0
        circleCount = 0
        while j < 3:
            while k < 3:
                k += 1
                circleCount += 1
                if circleCount > value:
                    continue
                xCirclePoint = xStartPoint +  circleSize[2] + 2 * (k-1) * circleSize[2]
                yCirclePoint = yStartPoint +  circleSize[2] + 2 * j * circleSize[2]
                drawingDevice.create_oval(xCirclePoint - circleSize[2], yCirclePoint - circleSize[2], xCirclePoint + circleSize[2], yCirclePoint + circleSize[2])
            j += 1
            k = 0
    actualColumn = 0
    actualRow += 1

mainloop()