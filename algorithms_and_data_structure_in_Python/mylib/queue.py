"""queue.py queue implement with list
"""
from .tree import BinaryHeap
import operator

__all__ = ["Queue", "PriorityQueue"]

class Queue:
    def __init__(self) -> None:
        self.__items = []

    def enqueue(self, item:object) -> None:
        self.__items.insert(0, item)

    def dequeue(self) -> None:
        self.__items.pop()

    def isEmpty(self) -> bool:
        return self.__items == []

    def size(self) -> int:
        return len(self.__items)

    def __str__(self) -> str:
        return str(self.__items)

class PriorityQueue:
    """
    Priority Queue implement with binary heap.
    """
    def __init__(self, prec = operator.lt) -> None:
        self.__pQueue = BinaryHeap(prec)
    
    def enqueue(self, item) -> None:
        self.__pQueue.insert(item)
    
    def dequeue(self) -> object:
        try:
            return self.__pQueue.delFirst()
        except IndexError:
            print("ERROR: CAN NOT DEQUEUE FROM EMPTY QUEUE.")