from time import time
from typing import Callable
from timeit import Timer

def wrap(n:int, func:Callable[[int], int]) -> tuple[int, float]:
    start = time()
    result = func(n)
    end = time()
    return result, end - start

def sumOfN(n:int) -> int:    
    theSum = 0
    for i in range(1, n + 1):
        theSum += i    
    return theSum

def sumOfN2(n:int) -> int:
    return (n*(n+1)) / 2

class AnagramSolver:
    
    @staticmethod
    def checkingMethod(s1:str, s2:str) -> bool:
        alist = list(s2)
        pos1 = 0
        stillOK = True
        # check every char in string s1
        while pos1 < len(s1) and stillOK:
            pos2 = 0
            found = False
            # check whether s1[pos1] in s2
            while pos2 < len(alist) and not found:
                if s1[pos1] == alist[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1
            if found:
                alist[pos2] = None
            else:
                stillOK = False
            pos1 = pos1 + 1
        return stillOK

    @staticmethod
    def sortingMethod(s1:str, s2:str) -> bool:
        alist1 = list(s1)
        alist2 = list(s2)
        alist1.sort()
        alist2.sort()
        pos = 0
        matches = True
        while pos < len(s1) and matches:
            if alist1[pos] == alist2[pos]:
                pos += 1
            else:
                matches = False
        return matches
    
    @staticmethod 
    def bruteForce(s1:str, s2:str) -> bool:
        pass

    @staticmethod
    def countingMethod(s1:str, s2:str) -> bool:
        c1 = [0] * 26
        c2 = [0 for x in range(26)]
        for i in range(len(s1)):
            pos = ord(s1[i]) - ord('a')
            c1[pos] += 1
        for i in range(len(s2)):
            pos = ord(s2[i]) - ord("a")
            c2[pos] += 1
        j = 0
        stillOK = True
        while j < 26 and stillOK:
            if c1[j] == c2[j]:
                j += 1
            else:
                stillOK = False
        return stillOK

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))



if __name__ == "__main__":
    t1 = Timer("test1()", "from __main__ import test1")
    print("concat\t\t", t1.timeit(number=1000), "\tms")

    t2 = Timer("test2()", "from __main__ import test2")
    print("append\t\t", t2.timeit(number=1000), "\tms")

    t3 = Timer("test3()", "from __main__ import test3")
    print("comprehension\t", t3.timeit(number=1000), "\tms")

    t4 = Timer("test4()", "from __main__ import test4")
    print("list range\t", t4.timeit(number=1000), "\tms")

    t5 = Timer()
    print("empty statement\t", t5.timeit(number=100000), "\tms")

    popzero = Timer("x.pop(0)", "from __main__ import x")
    popend = Timer("x.pop()", "from __main__ import x")
    print("--------------------")
    for i in range(1000000, 10000001, 1000000):
        print(f"[{i}]:")
        x = list(range(i))
        print("popend\t", popend.timeit(number=1000), "\tms")
        x = list(range(i))
        print("popzero\t", popzero.timeit(number=1000), "\tms")

