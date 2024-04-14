'''
Created on Apr 30, 2018

@author: felix
'''
from tkinter import Canvas, mainloop, Tk


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

HORIZONTAL_BORDER = 20
VERTICAL_BORDER = 20
INNER_BORDER = 5


def _GetRectangleSize(amount: int) -> tuple[int, int]:
    spaceX = WINDOW_WIDTH - 2 * HORIZONTAL_BORDER - (amount + 1) * INNER_BORDER
    spaceY = WINDOW_HEIGHT - 2 * VERTICAL_BORDER - (amount + 1) * INNER_BORDER
    horizontalSize = spaceX // amount
    verticalSize = spaceY // amount

    return horizontalSize, verticalSize


def _GetCircleSize(rectangleSizeX: int, rectangleSizeY: int) -> int:
        return min(rectangleSizeX, rectangleSizeY) // 6


def RenderMatrix(matrix: list[list[int]]) -> None:
    drawDev = Canvas(Tk(), width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    drawDev.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill = "#fff")
    drawDev.pack()

    horizontalSize, verticalSize = _GetRectangleSize(len(matrix))
    radius = _GetCircleSize(horizontalSize, verticalSize)

    for rowIdx, row in enumerate(matrix):
        for valueIdx, value in enumerate(row):

            startPointX = HORIZONTAL_BORDER + valueIdx * horizontalSize + INNER_BORDER * (valueIdx + 1)
            endPointX = HORIZONTAL_BORDER + (valueIdx + 1) * horizontalSize + INNER_BORDER * (valueIdx + 1)

            startPointY = VERTICAL_BORDER + rowIdx * verticalSize + INNER_BORDER * (rowIdx + 1)
            endPointY = VERTICAL_BORDER + (rowIdx + 1) * verticalSize + INNER_BORDER * (rowIdx + 1)

            drawDev.create_rectangle(startPointX, startPointY, endPointX, endPointY, outline = "#11eb11")

            offsetY = 0
            for i in range(value):
                if i and i % 3 == 0:
                    offsetY += 1

                centerX = startPointX + radius + 2 * (i % 3) * radius
                centerY = startPointY + radius + 2 * offsetY * radius
                drawDev.create_oval(centerX - radius, centerY - radius, centerX + radius, centerY + radius)

    mainloop()
