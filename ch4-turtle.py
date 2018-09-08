import turtle


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 5)


def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        # turn right and draw right branch
        t.right(20)
        tree(branchLen - 15, t)
        # turn left and draw left branch
        t.left(40)
        tree(branchLen - 15, t)
        # turn to middle and draw back
        t.right(20)
        t.backward(branchLen)


if __name__ == '__main__':
    # myTurtle = turtle.Turtle()
    # myWin = turtle.Screen()
    # drawSpiral(myTurtle, 100)
    # myWin.exitonclick()

    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()
