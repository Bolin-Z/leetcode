from mylib.tools import *
from typing import Any, Callable
from mylib.stack import Stack
import operator
import random

class BinaryTree:
    def __init__(self, rootObj:Any) -> None:
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, val:Any):
        self.key = val

    def getRootVal(self):
        return self.key

    def insertLeft(self, newNode:Any):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode:Any):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    
    @staticmethod
    def test():
        DEBUG.ON = True
        r = BinaryTree('a')
        DEBUG.PRINT(r.getRootVal())
        DEBUG.PRINT(r.getLeftChild())
        r.insertLeft('b')
        DEBUG.PRINT(r.getLeftChild())
        DEBUG.PRINT(r.getLeftChild().getRootVal())
        r.insertRight('c')
        DEBUG.PRINT(r.getRightChild())
        DEBUG.PRINT(r.getRightChild().getRootVal())
        r.getRightChild().setRootVal('hello')
        DEBUG.PRINT(r.getRightChild().getRootVal())

class BinaryTreeListVer:
    @staticmethod
    def BinaryTree(r) -> list:
        return [r, [], []]
    @staticmethod
    def insertLeft(root:list, newBranch) -> list:
        t = root.pop(1)
        if len(t) > 1:
            root.insert(1, [newBranch, t, []])
        else:
            root.insert(1, [newBranch, [], []])
        return root
    @staticmethod
    def insertRight(root:list, newBranch) -> list:
        t = root.pop(2)
        if len(t) > 1:
            root.insert(2, [newBranch, [], t])
        else:
            root.insert(2, [newBranch, [], []])
        return root
    @staticmethod
    def getRootVal(root):
        return root[0]
    @staticmethod
    def setRootVal(root:list, newVal):
        root[0] = newVal
    @staticmethod
    def getLeftChild(root:list):
        return root[1]
    @staticmethod
    def getRightChild(root:list):
        return root[2]
    
    @staticmethod
    def test():
        DEBUG.ON = True
        btl = BinaryTreeListVer()
        r = btl.BinaryTree(3)
        DEBUG.PRINT(btl.insertLeft(r, 4))
        DEBUG.PRINT(btl.insertLeft(r, 5))
        DEBUG.PRINT(btl.insertRight(r, 6))
        DEBUG.PRINT(btl.insertRight(r, 7))
        l = btl.getLeftChild(r)
        DEBUG.PRINT(l)
        btl.setRootVal(l, 9)
        DEBUG.PRINT(r)
        DEBUG.PRINT(btl.insertLeft(l, 11))
        DEBUG.PRINT(r)
        DEBUG.PRINT(btl.getRightChild(btl.getRightChild(r)))

def buildParseTree(fpexp:str) -> BinaryTree:
    """
    Convert full parenthese expression into expression tree
    :param fpexp: full parenthese expression to be converted
    :return: expression tree
    """
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in '+-*/)':
            currentTree.setRootVal(eval(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError("Unknown Operator: " + i)
    return eTree

def evaluate(parseTree:BinaryTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

def postordereval(tree:BinaryTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()

def printexp(tree:BinaryTree):
    """
    Print parse tree
    """
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + ' ' + str(tree.getRootVal()) + ' '
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal

def printexp2(tree:BinaryTree):
    sVal = ""
    lexp = tree.getLeftChild()
    rexp = tree.getRightChild()
    if lexp and rexp:
        sVal = '(' + printexp2(lexp) + ' ' + str(tree.getRootVal()) + ' ' + printexp2(rexp) + ')'
    else:
        sVal = str(tree.getRootVal())
    return sVal

def preorder(tree:BinaryTree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree:BinaryTree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree:BinaryTree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def parseTreeTest():
    DEBUG.ON = True
    x = BinaryTree('*')
    x.insertLeft('+')
    l = x.getLeftChild()
    l.insertLeft(4)
    l.insertRight(5)
    x.insertRight(7)
    DEBUG.PRINT(printexp(x))
    DEBUG.PRINT(printexp2(x))
    DEBUG.PRINT(postordereval(x))

class BinaryHeap:
    def __init__(self, prec = operator.lt) -> None:
        """
        Creat an empty binary heap.
        """
        # 0 is dummy item
        # for each x its parent is x // 2
        self.heapList = [0]
        self.currentSize = 0
        self.__prec = prec
    
    def __percUp(self, curIdx:int) -> None:
        parIdx = curIdx // 2
        while parIdx > 0:
            if self.__prec(self.heapList[curIdx], self.heapList[parIdx]):
                self.heapList[curIdx], self.heapList[parIdx] = self.heapList[parIdx], self.heapList[curIdx]
            curIdx = parIdx
            parIdx = parIdx // 2                

    def __percDown(self, curIdx:int) -> None:
        childIdx = curIdx * 2
        while childIdx <= self.currentSize:
            pc = self.__precChild(curIdx)
            if self.__prec(self.heapList[pc], self.heapList[curIdx]):
                self.heapList[curIdx], self.heapList[pc] = self.heapList[pc], self.heapList[curIdx]
            curIdx = pc
            childIdx = pc * 2

    def __precChild(self, curidx:int):
        if curidx * 2 + 1 > self.currentSize:
            return curidx * 2
        else:
            return curidx * 2 if self.__prec(self.heapList[curidx * 2], self.heapList[curidx * 2 + 1]) else curidx * 2 + 1
    
    def insert(self, e) -> None:
        """
        Insert a new element into heap.
        :param e: Element to be inserted.
        """
        self.heapList.append(e)
        self.currentSize += 1
        self.__percUp(self.currentSize)

    def findMin(self) -> Any:
        """
        Find the minimum element in the heap and return it.
        """
        retVal = self.heapList[1]
        return retVal
    
    def delMin(self) -> Any:
        """
        Delete the minimum element in the heap and return it.
        """
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.__percDown(1)
        return retVal

    def isEmpty(self) -> bool:
        return self.currentSize == 0

    def size(self) -> int:
        return self.currentSize

    def buildHeap(self, alist:list) -> None:
        """
        Construct a binary heap from a list
        """
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.__percDown(i)
            i = i - 1

    @staticmethod
    def test() -> None:
        DEBUG.ON = True
        bh = BinaryHeap()
        bh.insert(5)
        bh.insert(7)
        bh.insert(3)
        bh.insert(11)
        DEBUG.PRINT(bh.delMin())
        DEBUG.PRINT(bh.delMin())
        DEBUG.PRINT(bh.delMin())
        DEBUG.PRINT(bh.delMin())

def heapSort(alist:list, prec = operator.lt) -> None:
    bh = BinaryHeap(prec)
    bh.buildHeap(alist)
    for i in range(len(alist)):
        alist[i] = bh.delMin()

def cmp(a:int, b:int) -> bool:
    if (a % 2 == 1 and b % 2 == 1) or (a % 2 == 0 and b % 2 == 0):
        return a < b
    else:
        return a % 2 == 1

if __name__ == "__main__":
    a = []
    for i in range(10):
        a.append(random.randrange(0, 100))
    DEBUG.ON = True
    DEBUG.PRINT(a)
    heapSort(a, cmp)
    DEBUG.PRINT(a)