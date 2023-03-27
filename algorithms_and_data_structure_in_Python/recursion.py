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

# exercise 4-1
def factorial(n:int)->int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# exercise 4-9
def fillWater(maxA:int, maxB:int, target:int) -> None:
    solution:list[tuple[str,int,int]] = []
    
    def __tracebackTry(state:tuple[str, int, int]) -> bool:
        if solution.count(state) == 0:
            solution.append(state)
            if __solution(state[1], state[2]):
                return True
            solution.pop()
        return False

    def __solution(curA:int, curB:int) -> bool:
        if curA == target or curB == target:
            return True
        else:
            if curA < maxA:
                state = ("Fill A", maxA, curB)
                if __tracebackTry(state):
                    return True
            if curA > 0:
                nxtA = max(0, curA - (maxB - curB))
                nxtB = min(maxB, curB + curA)
                state = ("Pour A to B", nxtA, nxtB)
                if __tracebackTry(state):
                    return True
                nxtA = 0
                nxtB = curB
                state = ("Empty A", nxtA, nxtB)
                if __tracebackTry(state):
                    return True
            if curB < maxB:
                state = ("Fill B", curA, maxB)
                if __tracebackTry(state):
                    return True
            if curB > 0:
                nxtA = min(maxA, curA + curB)
                nxtB = max(0, curB - (maxA - curA))
                state = ("Pour B to A", nxtA, nxtB)
                if __tracebackTry(state):
                    return True
                nxtA = curA
                nxtB = 0
                state = ("Empty B", nxtA, nxtB)
                if __tracebackTry(state):
                    return True
            return False
    
    solution.append(("Initial", 0, 0))
    if __solution(0, 0):
        for idx, s in enumerate(solution):
            action, stateA, stateB = s
            print(f"step{idx}: {action}")
            print(f"  A:{'w' * stateA}|({stateA})")
            print(f"  B:{'w' * stateB}|({stateB})")
    else:
        print("No solution")

# exercise 4-11
def MCsolver(totalM:int, totalC:int) -> None:
    LEFT = True
    RIGHT = False
    solution:list[tuple[int,int,bool]] = []

    def __isLegal(M:int, C:int) -> bool:
        rightM = totalM - M
        rightC = totalC - C
        if M < 0 or C < 0 or rightM < 0 or rightC < 0:
            return False
        elif ((M != 0) and (C > M)) or ((rightM != 0) and (rightC > rightM)):
            return False
        else:
            return True
    
    def __computeState(state:tuple[int, int, bool]) -> tuple[int, int, int, int, bool]:
        leftM, leftC, boat = state
        return (leftM, leftC, totalM - leftM, totalC - leftC, boat)

    def __solution(curM:int, curC:int, curBoat:bool) -> bool:
        curState = (curM, curC, curBoat)
        if curM == 0 and curC == 0 and curBoat == RIGHT:
            solution.append(curState)
            return True
        else:
            if __isLegal(curM, curC) and solution.count(curState) == 0:
                solution.append(curState)
                delta2 = -2 if curBoat == LEFT else 2
                delta1 = -1  if curBoat == LEFT else 1
                if __solution(curM + delta2, curC, not curBoat):
                    return True
                if __solution(curM, curC + delta2, not curBoat):
                    return True
                if __solution(curM + delta1, curC, not curBoat):
                    return True
                if __solution(curM, curC + delta1, not curBoat):
                    return True
                if __solution(curM + delta1, curC + delta1, not curBoat):
                    return True
                solution.pop()
            return False

    if __solution(totalM, totalC, LEFT):
        if totalM >= totalC:
            intervalM = totalM + 2
            intervalC = 2 * totalM - totalC + 2
        else:
            intervalM = 2 * totalC - totalM + 2
            intervalC = totalC + 2

        for idx in range(len(solution)):
            curLeftM, curLeftC, curRightM, curRightC, curBoat = __computeState(solution[idx])
            print(f"step ({idx})")
            if idx != len(solution) - 1:
                nxtLeftM, nxtLeftC, nxtRightM, nxtRightC, nxtBoat = __computeState(solution[idx + 1])
                if curBoat == LEFT:
                    infoM = "" if nxtRightM == curRightM else f"--> {nxtRightM - curRightM} M"
                    infoC = "" if nxtRightC == curRightC else f"--> {nxtRightC - curRightC} C"
                    print(f" B M:|{'m' * curLeftM + ' ' * intervalM + 'm' * curRightM}|   {infoM}")
                    print(f"   C:|{'c' * curLeftC + ' ' * intervalC + 'c' * curRightC}|   {infoC}")
                else:
                    infoM = "" if nxtLeftM == curLeftM else f"<-- {nxtLeftM - curLeftM} M"
                    infoC = "" if nxtLeftC == curLeftC else f"<-- {nxtLeftC - curLeftC} C"
                    print(f"   M:|{'m' * curLeftM + ' ' * intervalM + 'm' * curRightM}| B {infoM}")
                    print(f"   C:|{'c' * curLeftC + ' ' * intervalC + 'c' * curRightC}|   {infoC}")
            else:
                print(f"   M:|{'m' * curLeftM + ' ' * intervalM + 'm' * curRightM}| B")
                print(f"   C:|{'c' * curLeftC + ' ' * intervalC + 'c' * curRightC}|")
    else:
        print("No solution")

# exercise 4-14
def backPack(items:list[tuple[int, int]], capacity:int) -> int:
    dp = [[0 for i in range(capacity + 1)] for j in range(len(items) + 1)]
    for i in range(len(items)):
        weight, value = items[i]
        for v in range(capacity + 1):
            dp[i][v] = dp[i - 1][v]
            if v >= weight:
                dp[i][v] = max(dp[i - 1][v], dp[i - 1][v - weight] + value)
    return dp[len(items) - 1][capacity]

def backPack2(items:list[tuple[int, int]], capacity:int) -> int:
    dp = [0 for i in range(capacity + 1)]
    for i in range(len(items)):
        weight, value = items[i]
        for v in range(capacity, weight - 1, -1):
            dp[v] = max(dp[v], dp[v - weight] + value)
    return dp[capacity]


if __name__ == "__main__":
    MCsolver(4,4)