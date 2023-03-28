from tools import *

DEBUG.ON = False

def bubbleSort(alist:list) -> None:
    """
    :param alist: list of comparable objects
    :return:
    """
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                # temp = alist[i]
                # alist[i] = alist[i + 1]
                # alist[i + 1] = temp
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

def shortBubbleSort(alist:list) -> None:
    """
    :param alist: list of comparable objects
    :return:
    """
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum = passnum - 1

def selectionSort(alist:list) -> None:
    """
    :param alist: list of comparable objects
    :return:
    """
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]

def insertionSort(alist:list) -> None:
    """
    :param alist: list of comparable objects
    :return:
    """
    for index in range(1, len(alist)):
        # value to be inseted in this round
        currentvalue = alist[index]
        position = index
        # find position to insert
        while position > 0 and alist[position -1] > currentvalue:
            # shifting
            alist[position] = alist[position -1]
            position = position - 1
        
        alist[position] = currentvalue

class ShellSort:
    @staticmethod
    def shellSort(alist:list) -> None:
        """
        :param alist: list of comparable objects
        :return:
        """
        sublistcount = len(alist) // 2
        while sublistcount > 0:
            for startposition in range(sublistcount):
                ShellSort.__gapInsertionSort(alist, startposition, sublistcount)
            sublistcount = sublistcount // 2
    
    @staticmethod
    def __gapInsertionSort(alist:list, start:int, gap:int) -> None:
        for i in range(start + gap, len(alist), gap):
            currentvalue = alist[i]
            position = i
            while position >= gap and alist[position - gap] > currentvalue:
                alist[position] = alist[position - gap]
                position = position - gap
            alist[position] = currentvalue

def mergeSort(alist:list) -> None:
    """
    :param alist: list of comparable objects
    :return:
    """
    DEBUG.PRINT("Spliting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1
        
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    DEBUG.PRINT("Merging  ", alist)

# @TIMER()
def mergeSort2(alist:int, start:int, end:int) -> None:
    """
    :param alist: list of comparable objects
    :param start: start index of interval being sorted
    :param end: end index of interval being sorted but not included
    :return:
    """
    DEBUG.PRINT("Spliting ", alist[start:end])
    if end - start > 1:
        mid = (start + end) // 2

        mergeSort2(alist, start, mid)
        mergeSort2(alist, mid, end)

        i = start
        j = mid
        t = []
        while i < mid and j < end:
            if alist[i] < alist[j]:
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

    DEBUG.PRINT("Merging  ", alist[start:end])

class QuickSort:
    @staticmethod
    def quickSort(alist:list) -> None:
        QuickSort.__quickSortHelper(alist, 0, len(alist) - 1)

    @staticmethod
    def __quickSortHelper(alist:list, first:int, last:int) -> None:
        if first < last:
            splitpoint = QuickSort.__partition(alist, first, last)
            QuickSort.__quickSortHelper(alist, first, splitpoint - 1)
            QuickSort.__quickSortHelper(alist, splitpoint + 1, last)

    @staticmethod
    def __partition(alist:list, first:int, last:int) -> int:
        # a dummy way to choose a pivot
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last
        done = False
        while not done:
            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
            while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
                rightmark = rightmark - 1
            
            if rightmark < leftmark:
                done = True
            else:
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
        
        alist[first], alist[rightmark] = alist[rightmark], alist[first]
        return rightmark

if __name__ == "__main__":
    b = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort2(b, 0, len(b))