import functools
from stack import Stack
from typing import Callable
from turtle import *

def listsum(numList:list[int]) -> int:
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

def toStr(n, base):
    """
    Convert demical number n to base-x number
    """
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

def toStr2(n:int, base:int) -> str:
    rStack = Stack()
    result = ""
    
    def __toStr2(__n:int, __base:int) -> str:
        convertString = "0123456789ABCDEF"
        if __n < __base:
            rStack.push(convertString[__n])
        else:
            rStack.push(convertString[__n % __base])
            __toStr2(__n//__base, __base)

    __toStr2(n, base)
    while not rStack.isEmpty():
        result += rStack.pop()
    return result

def drawSpiral(len:int) -> None:
    myTurtle = Turtle()
    myWin = myTurtle.getscreen()

    def __drawSpiral(myTurtle:Turtle, lineLen:float) -> None:
        if lineLen > 0:
            myTurtle.forward(lineLen)
            myTurtle.right(90)
            __drawSpiral(myTurtle, lineLen - 5)
    
    __drawSpiral(myTurtle, len)
    myWin.exitonclick()

def drawTree(len:int) -> None:
    t = Turtle()
    myWin = t.getscreen()

    def __drawTree(t:Turtle, branchLen:float) -> None:
        if branchLen > 5:
            t.forward(branchLen)
            t.right(30)
            __drawTree(t, branchLen - 15)
            t.left(60)
            __drawTree(t, branchLen - 10)
            t.right(30)
            t.backward(branchLen)

    t.left(90)
    t.up()
    t.backward(300)
    t.down()
    t.color("green")
    __drawTree(t, len)
    myWin.exitonclick()

def drawSierpinski(points:list[tuple[float]], degree:int) -> None:
    def drawTriangle(points:list[tuple[float]], color:str, myTurtle:Turtle) -> None:
        myTurtle.fillcolor(color)
        myTurtle.up()
        myTurtle.goto(points[0])
        myTurtle.down()
        myTurtle.begin_fill()
        myTurtle.goto(points[1])
        myTurtle.goto(points[2])
        myTurtle.goto(points[0])
        myTurtle.end_fill()
    
    def getMid(p1:tuple[float], p2:tuple[float]) -> tuple[float]:
        return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    
    def sierpinski(points:list[tuple[float]], degree:int, myTurtle:Turtle) -> None:
        colormap = [
            "blue", "red", "green", "white",
            "yellow", "violet", "orange"
        ]
        drawTriangle(points, colormap[degree % len(colormap)], myTurtle)
        if degree > 0:
            sierpinski(
                [
                    points[0], getMid(points[0], points[1]), getMid(points[0], points[2])
                ],
                degree - 1,
                myTurtle
            )
            sierpinski(
                [
                    points[1], getMid(points[0], points[1]), getMid(points[1], points[2])
                ],
                degree - 1,
                myTurtle
            )
            sierpinski(
                [
                    points[2], getMid(points[2], points[1]), getMid(points[0], points[2])
                ],
                degree - 1,
                myTurtle
            )
    
    myTurtle = Turtle()
    myWin = myTurtle.getscreen()
    sierpinski(points, degree, myTurtle)
    myWin.exitonclick()

def hanoiTower(height:int) -> None:
    pole = "ABC"
    def moveDisk(diskNum:int, fromPole:int, toPole:int) -> None:
        print(f"move disk({diskNum}) from {pole[fromPole]} to {pole[toPole]}")
    
    def moveTower(height:int, fromPole:int, toPole:int, withPole:int) -> None:
        if height >= 1:
            moveTower(height - 1, fromPole, withPole, toPole)
            moveDisk(height, fromPole, toPole)
            moveTower(height - 1, withPole, toPole, fromPole)

    moveTower(height, 0, 2, 1)

if __name__ == "__main__":
    pass