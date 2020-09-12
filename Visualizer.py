from ParserOOP import parseToTree
from Node import Node, Num, Var
import turtle

windowSizeX = 1700
windowSizeY = 1000
def drawNode(x, y, node, spacingX, spacingY):
    if type(node) in [int, float, Num]:
        toDraw = int(node)
    else:
        toDraw = node.op

    fontSize = int(1.2 * circleR / (len(str(toDraw))))
    pen.penup()
    pen.setheading(0)
    pen.setposition(x, y)
    pen.pendown()

    pen.pensize(5)
    pen.circle(circleR)
    pen.pensize(1)
    pen.write(str(toDraw).replace("/", "÷"), font=("Cascadia", fontSize, ""), align="center")

    leftNodePos = [x-spacingX, y-spacingY]
    rightNodePos = [x+spacingX, y-spacingY]

    if type(node) not in [float, int, Num, Var]:
        pen.penup()
        pen.setposition(x-circleR*1.5, y+circleR*0.3)
        pen.pendown()
        pen.pensize(5)
        pen.setposition(leftNodePos[0]+circleR, leftNodePos[1]+circleR*2/1.1)
        pen.pensize(1)
        pen.penup()
        drawNode(leftNodePos[0], leftNodePos[1], node.left, spacingX / 1.5, spacingY*1.5)

        pen.penup()
        pen.setposition(x + circleR * 1.5, y + circleR * 0.3)
        pen.pendown()
        pen.pensize(5)
        pen.setposition(rightNodePos[0]-circleR, rightNodePos[1]+circleR*2/1.1)
        pen.pensize(1)
        pen.penup()

        drawNode(rightNodePos[0], rightNodePos[1], node.right, spacingX / 1.5, spacingY*1.5)


circleR = 40  # len(expr)/0.001
startX = 0
spacingX = circleR * 6 + 10
spacingY = circleR * 2 + 10

def visualizeExprTree(*, expr=None, obj=None):
    global pen
    global scr
    pen = turtle.Turtle()
    scr = turtle.Screen()
    scr.bgcolor("#000000")
    pen.pencolor("#ffffff")
    pen.speed(0)

    scr.setup(windowSizeX, windowSizeY, startx=100, starty=10)
    if not obj:
        obj = parseToTree(expr, False)
    startY = windowSizeY / 2 - circleR * 2 - 10
    drawNode(startX, startY, obj, spacingX, spacingY)
    pen.hideturtle()
    scr.exitonclick()


if __name__ == '__main__':
    expr = input("Enter expr: ")
    visualizeExprTree(expr=expr)