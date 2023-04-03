"""sorting.py sorting method
"""
from .tree import heapSort
import operator

__all__ = ["heapSort", "bubbleSort", "shortBubbleSort", "selectionSort",
    "insertionSort", "shellSort", "mergeSort", "quickSort"
]

def bubbleSort(alist:list, prec = operator.lt, reverse = False) -> None:
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if prec(alist[i + 1], alist[i]) ^ reverse:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

def shortBubbleSort(alist:list, prec = operator.lt, reverse = False) -> None:
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if prec(alist[i + 1], alist[i]) ^ reverse:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum = passnum - 1

def selectionSort(alist:list, prec = operator.lt, reverse = False) -> None:
    for fillslot in range(len(alist) - 1, 0, -1):
        positionToBeExchange = 0
        for location in range(1, fillslot + 1):
            if prec(alist[positionToBeExchange], alist[location]) ^ reverse:
                positionToBeExchange = location
        alist[fillslot], alist[positionToBeExchange] = alist[positionToBeExchange], alist[fillslot]

def insertionSort(alist:list, prec = operator.lt, reverse = False) -> None:
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and (prec(currentvalue, alist[position - 1]) ^ reverse):
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = currentvalue

def shellSort(alist:list, prec = operator.lt, reverse = False) -> None:
    def __gapInsertionSort(alist:list, start:int, gap:int) -> None:
        nonlocal prec, reverse
        for i in range(start + gap, len(alist), gap):
            currentvalue = alist[i]
            position = i
            while position >= gap and (prec(currentvalue, alist[position - gap]) ^ reverse):
                alist[position] = alist[position - gap]
                position = position - gap
            alist[position] = currentvalue
    
    sublistcount = len(alist) // 2
    while sublistcount > 0 :
        for startposition in range(sublistcount):
            __gapInsertionSort(alist, startposition, sublistcount)
        sublistcount = sublistcount // 2

def mergeSortCopy(alist:list, prec = operator.lt, reverse = False) -> None:
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSortCopy(lefthalf)
        mergeSortCopy(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if prec(lefthalf[i], righthalf[j]) ^ reverse:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def mergeSort(alist:list, prec = operator.lt, reverse = False) -> None:
    def __mergeSort(alist:list, start:int, end:int) -> None:
        nonlocal prec, reverse
        if end - start > 1:
            mid = (start + end) // 2

            __mergeSort(alist, start, mid)
            __mergeSort(alist, mid, end)

            i = start
            j = mid
            t = []

            while i < mid and j < end:
                if prec(alist[i], alist[j]) ^ reverse:
                    t.append(alist[i])
                    i += 1
                else:
                    t.append(alist[j])
                    j += 1
            while i < mid:
                t.append(alist[i])
                i += 1
            while j < end:
                t.append(alist[j])
                j += 1
            
            k = start
            for i in t:
                alist[k] = i
                k += 1
    __mergeSort(alist, 0, len(alist))

def quickSort(alist:list, prec = operator.lt, reverse = False) -> None:
    def __quickSortHelper(alist:list, first:int, last:int) -> None:
        if first < last:
            splitpoint = __partition(alist, first, last)
            __quickSortHelper(alist, first, splitpoint - 1)
            __quickSortHelper(alist, splitpoint + 1, last)

    def __partition(alist:list, first:int, last:int) -> int:
        nonlocal prec, reverse
        pivotvalue = alist[first]
        leftmark = first + 1
        rightmark = last
        done = False
        while not done:
            while leftmark <= rightmark and (not(prec(pivotvalue, alist[leftmark])) ^ reverse):
                leftmark = leftmark + 1
            while rightmark >= leftmark and (not(prec(alist[rightmark], pivotvalue)) ^ reverse):
                rightmark = rightmark - 1
            
            if rightmark < leftmark:
                done = True
            else:
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
        alist[first], alist[rightmark] = alist[rightmark], alist[first]
        return rightmark
    
    __quickSortHelper(alist, 0, len(alist) - 1)