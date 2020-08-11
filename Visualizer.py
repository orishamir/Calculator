from ParserWithTree import parseToTree
from CalculationTree import Node, Num
import turtle

expr = input("Enter expr: ")

pen = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("#000000")
pen.pencolor("#ffffff")
pen.speed(2)
windowSizeX = 1700
windowSizeY = 1000

scr.setup(windowSizeX, windowSizeY, startx=100, starty=10)


def drawNode(x, y, node, spacingX, spacingY):
    if type(node) is Num:
        toDraw = int(node.val)
    elif type(node) in [int, float]:
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
    pen.write(str(toDraw).replace("/", "÷").replace("*", '×'), font=("Cascadia", fontSize, ""), align="center")

    if isinstance(node, Node):
        pen.penup()
        pen.setposition(x - circleR * 1.5, y + circleR * 0.3)
        pen.pendown()
        pen.pensize(5)
        pen.setposition(x - spacingX + circleR * 1.5, y - spacingY + circleR * 1.5)
        pen.pensize(1)
        pen.penup()
        drawNode(x - spacingX, y - spacingY, node.left, spacingX / 2, spacingY)

        pen.penup()
        pen.setposition(x + circleR * 1.5, y + circleR * 0.3)
        pen.pendown()
        pen.pensize(5)
        pen.setposition(x + spacingX - circleR * 1.5, y - spacingY + circleR * 1.5)
        pen.pensize(1)
        pen.penup()

        drawNode(x + spacingX, y - spacingY, node.right, spacingX / 2, spacingY)


circleR = 40  # len(expr)/0.001
startX = 0
startY = windowSizeY / 2 - circleR * 2 - 10
spacingX = circleR * 6 + 10
spacingY = circleR * 2 + 10

n = parseToTree(expr, False)
drawNode(startX, startY, n, spacingX, spacingY)
pen.hideturtle()
scr.exitonclick()
