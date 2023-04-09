"""tree.py
"""
import operator

__all__ = ["BinaryTree", "BinaryHeap", "heapSort", "BinarySearchTree", "AVLTree"]

class BinaryTree:
    """
    Binary tree
    """
    def __init__(self, rootval:object) -> None:
        self.key = rootval
        self.leftChild : BinaryTree|None = None
        self.rightChild : BinaryTree|None = None
        
    def getLeftChild(self):
        """
        Return the left sub binary tree of current node.
        """
        return self.leftChild

    def getRightChild(self):
        """
        Return the right sub binary tree of current node.
        """
        return self.rightChild

    def getRootVal(self) -> object:
        """
        Return the value stored in current node.
        """
        return self.key

    def setRootVal(self, val:object) -> None:
        """
        Stored val in current node.
        """
        self.key = val

    def insertLeft(self, val:object) -> None:
        """
        Insert a new binary tree with root value val as the left child of current node.
        """
        if self.leftChild == None:
            self.leftChild = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, val:object) -> None:
        """
        Insert a new binary tree with root value val as the right child of current node.
        """
        if self.rightChild == None:
            self.rightChild = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.rightChild = self.rightChild
            self.rightChild = t

class BinaryHeap:
    """
    Binary heap implement with list.
    """
    def __init__(self, prec = operator.lt) -> None:
        # 0 is dummy item
        # for each x its parent is x // 2
        self.__heapList = [0]
        self.__currentSize = 0
        self.__prec = prec
    
    def __str__(self) -> str:
        return str(self.__heapList[1:])
    
    def __percUp(self, curIdx:int) -> None:
        parIdx = curIdx // 2
        while parIdx > 0:
            if self.__prec(self.__heapList[curIdx], self.__heapList[parIdx]):
                self.__heapList[curIdx], self.__heapList[parIdx] = self.__heapList[parIdx], self.__heapList[curIdx]
            curIdx = parIdx
            parIdx = parIdx // 2
    
    def __percDown(self, curIdx:int) -> None:
        childIdx = curIdx * 2
        while childIdx <= self.__currentSize:
            pc = self.__precChild(curIdx)
            if self.__prec(self.__heapList[pc], self.__heapList[curIdx]):
                self.__heapList[curIdx], self.__heapList[pc] = self.__heapList[pc], self.__heapList[curIdx]
            curIdx = pc
            childIdx = pc * 2

    def __precChild(self, curIdx:int) -> int:
        if curIdx * 2 + 1 > self.__currentSize:
            return curIdx * 2
        else:
            return curIdx * 2 if self.__prec(self.__heapList[curIdx * 2], self.__heapList[curIdx * 2 + 1]) else curIdx * 2 + 1
    
    def insert(self, e) -> None:
        """
        Insert a new element into heap.
        :param e: Element to be inserted.
        """
        self.__heapList.append(e)
        self.__currentSize += 1
        self.__percUp(self.__currentSize)

    def findFirst(self) -> object:
        """
        Find the first element in the heap and return it.
        """
        try:
            return self.__heapList[1]
        except IndexError:
            print("ERROR: THE HEAP IS EMPTY.")
    
    def delFirst(self) -> object:
        """
        Delete the first element in the heap and return it.
        """
        try:
            retVal = self.__heapList[1]
            self.__heapList[1] = self.__heapList[self.__currentSize]
            self.__currentSize -= 1
            self.__heapList.pop()
            self.__percDown(1)
            return retVal
        except IndexError:
            print("ERROR: CAN NOT DELETE ELEMENT FROM EMPTY HEAP.")
    
    def buildHeap(self, alist:list) -> None:
        """
        Construct a binary heap from a list.
        """
        i = len(alist) // 2
        self.__currentSize = len(alist)
        self.__heapList = [0] + alist[:]
        while i > 0:
            self.__percDown(i)
            i = i - 1
    
    def isEmpty(self) -> bool:
        return self.__currentSize == 0
    
    def size(self) -> int:
        return self.__currentSize

    def __len__(self) -> int:
        return self.__currentSize

def heapSort(alist:list, prec = operator.lt) -> None:
    """
    Sort list using heap.
    :param alist: list to be sorted
    :param prec: precedence function
    """
    bh = BinaryHeap(prec)
    bh.buildHeap(alist)
    for i in range(len(alist)):
        alist[i] = bh.delFirst()

class TreeNode:
    def __init__(self, key:object, val:object, left:"TreeNode" = None, \
        right:"TreeNode" = None, parent:"TreeNode" = None, \
            balanceFactor:int = 0) -> None:
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = balanceFactor
    
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild: # recursion here __iter__()
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
    
    def hasLeftChild(self) -> bool:
        return self.leftChild != None
    
    def hasRightChild(self) -> bool:
        return self.rightChild != None
    
    def isLeftChild(self) -> bool:
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self) -> bool:
        return self.parent and self.parent.rightChild == self
    
    def isRoot(self) -> bool:
        return not self.parent
    
    def isLeaf(self) -> bool:
        return not self.hasAnyChildren()
    
    def hasAnyChildren(self) -> bool:
        return self.rightChild or self.leftChild
    
    def hasBothChildren(self) -> bool:
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self, key, val, lc:"TreeNode", rc:"TreeNode") -> None:
        self.key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
    
    def findSuccessor(self) -> "TreeNode":
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    
    def findMin(self) -> "TreeNode":
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    
    def spliceOut(self) -> None:
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        else:
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: TreeNode = None
        self.__size = 0

    def length(self):
        return self.__size

    def __str__(self) -> str:
        return self.display(self.root, 0) if self.root else "[]"

    def display(self, currentnode:TreeNode, depth:int) -> str:
        res = ""
        width = 10
        if currentnode.hasRightChild():
            res = res + self.display(currentnode.rightChild, depth + 1)
        res = res + " " * width * depth
        if currentnode.isRightChild():
            res += "/"
        elif currentnode.isLeftChild():
            res += "\\"
        res = res + "[" + str(currentnode.key) + "]:" + str(currentnode.payload) + "(" + str(currentnode.balanceFactor) + ")\n" 
        if currentnode.hasLeftChild():
            res = res + self.display(currentnode.leftChild, depth + 1)
        return res

    def __len__(self):
        return self.__size
    
    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, k, v) -> None:
        self.put(k, v)

    def __getitem__(self, key) -> object:
        return self.get(key)

    def __delitem__(self, key) -> None:
        self.delete(key)
    
    def __contains__(self, key) -> bool:
        return self._get(key, self.root) != None
    
    def put(self, key, val) -> None:
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.__size = self.__size + 1

    def _put(self, key, val, currentNode:TreeNode) -> None:
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        elif key == currentNode.key:
            currentNode.payload = val
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
    
    def get(self, key) -> object:
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    
    def _get(self, key, currentNode:TreeNode) -> TreeNode:
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)
    
    def delete(self, key) -> None:
        if self.__size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.__size = self.__size - 1
            else:
                raise KeyError('Error, key not in tree.')
        elif self.__size == 1 and self.root.key == key:
            self.root = None
            self.__size = self.__size - 1
        else:
            raise KeyError('Error, key not in tree.')
    
    def remove(self, currentNode:TreeNode) -> None:
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: # has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else: # current node is root
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild
                    )
            else: # has right child
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild
                    )

class AVLTree(BinarySearchTree):
    def _put(self, key, val, currentNode:TreeNode) -> None:
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        elif key == currentNode.key:
            currentNode.payload = val
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node:TreeNode) -> None:
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)
    
    def rebalance(self, node:TreeNode) -> None:
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def rotateLeft(self, rotRoot:TreeNode) -> None:
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)
    
    def rotateRight(self, rotRoot:TreeNode) -> None:
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)
    
    def updateBalance2(self, node:TreeNode) -> None:
        if node.balanceFactor != 1 and node.balanceFactor != -1:
            parent = node.parent
            if parent != None:
                if node.isLeftChild():
                    node.parent.balanceFactor -= 1
                elif node.isRightChild():
                    node.parent.balanceFactor += 1
            if node.balanceFactor > 1 or node.balanceFactor < -1:
                self.rebalance(node)
            if parent != None:
                self.updateBalance2(parent)

    def remove(self, currentNode: TreeNode) -> None:
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
                currentNode.parent.balanceFactor -= 1
            else:
                currentNode.parent.rightChild = None
                currentNode.parent.balanceFactor += 1
            self.updateBalance2(currentNode.parent)
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            self.remove(succ)
        else: # has one child and must be leaf
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                    currentNode.parent.balanceFactor -= 1
                    self.updateBalance2(currentNode.parent)
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.parent.balanceFactor += 1
                    self.updateBalance2(currentNode.parent)
                else: # current node is root
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild
                    )
                    currentNode.balanceFactor = 0
            else: # has right child
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.parent.balanceFactor -= 1
                    self.updateBalance2(currentNode.parent)
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.parent.balanceFactor += 1
                    self.updateBalance2(currentNode.parent)
                else: # current node is root
                    currentNode.replaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild
                    )
                    currentNode.balanceFactor = 0