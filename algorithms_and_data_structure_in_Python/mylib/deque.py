"""deque.py deque implement with list
"""

__all__ = ['Deque']

class Deque:
    """
    Double-ended queue implement with list.
    """
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self) -> bool:
        return self.items == []
    
    def size(self) -> int:
        return len(self.items)

    def addFront(self, item:object) -> None:
        """
        Add item in the front of deque.
        """
        self.items.append(item)
    
    def addRear(self, item:object) -> None:
        """
        Add item in the end of deque.
        """
        self.items.insert(0, item)
    
    def removeFront(self) -> object:
        """
        Remove the first item and return it.
        """
        return self.items.pop()
    
    def removeRear(self) -> object:
        """
        Remove the last item and return it.
        """
        return self.items.pop(0)
