"""list.py - linked list data structure
"""

__all__ = ["List", "OrderList"]

from typing import Union

class Node:
    def __init__(self, data:object) -> None:
        self.__data = data
        self.__next:Node = None
    
    @property
    def data(self) -> object:
        return self.__data
    
    @data.setter
    def data(self, newdata:object) -> None:
        self.__data = newdata
    
    @property
    def next(self) -> "Node":
        return self.__next
    
    @next.setter
    def next(self, newnext:"Node") -> None:
        self.__next = newnext

class List:
    """
    Unorder linked list.
    """
    def __init__(self) -> None:
        self.__head = None
    
    def isEmpty(self) -> bool:
        return self.__head == None
    
    def add(self, item:object) -> None:
        """
        Add an item into the head of list.
        """
        temp = Node(item)
        temp.next = self.__head
        self.__head = temp
    
    def remove(self, item:object) -> None:
        """
        Remove the item from list if exists.
        """
        current = self.__head
        previous = None
        found = False
        stop = False
        while not found and not stop:
            if current == None:
                stop = True
            else:
                if current.data == item:
                    found = True
                else:
                    previous = current
                    current = current.next
        if found:
            if previous == None:
                self.__head = current.next
            else:
                previous.next = current.next
        else:
            raise KeyError

    def search(self, item:object) -> bool:
        """
        Search item in list and return whether it exists
        """
        current = self.__head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def length(self) -> int:
        current = self.__head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    
    def append(self, item:object) -> None:
        """
        Add an item in the tail of list.
        """
        current = self.__head
        previous = None
        while current != None:
            previous = current
            current = current.next
        temp = Node(item)
        if previous == None:
            self.__head = temp
        else:
            previous.next = temp

    def index(self, item:object) -> int:
        """
        Return first index of item
        """
        current = self.__head
        found = False
        idx = 0
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
                idx = idx + 1
        if found:
            return idx
        else:
            raise ValueError

    def insert(self, pos:int, item:object) -> None:
        curlen = self.length()
        temp = Node(item)
        if pos < -curlen:
            temp.next = self.__head
            self.__head = temp.next
        else:
            if pos < 0:
                pos = pos + curlen
            current = self.__head
            previous = None
            while pos != 0 and current != None:
                previous = current
                current = current.next
                pos = pos - 1
            if previous == None:
                self.__head = temp
            else:
                previous.next = temp
                temp.next = current

    def pop(self, pos:int = -1) -> object:
        curlen = self.length()
        if pos < 0:
            pos = pos + curlen
        if pos >= 0 and pos < curlen:
            current = self.__head
            previous = None
            while pos != 0:
                previous = current
                current = current.next
                pos -= 1
            if previous == None:
                self.__head = current.next
            else:
                previous.next = current.next
            return current
        else:
            raise IndexError
    
    def __str__(self) -> str:
        res = "["
        if not self.isEmpty():
            res = res + str(self.__head.data)
            current = self.__head.next
            while current != None:
                res = res + ', ' + str(current.data)
                current = current.next
        res = res + ']'
        return res

    def __len__(self) -> int:
        return self.length()
    
    def __getitem__(self, idx:int) -> object | None:
        pass
    
    def __delitem__(self, idx:int):
        pass
    
    def __contains__(self, key:object) -> bool:
        return self.search(key)

class OrderList:
    def __init__(self) -> None:
        self.__head:Node = None

    def add(self, item:object) -> None:
        current = self.__head
        previous = None
        stop = False
        while current != None and not stop:
            if current.data > item:
                stop = True
            else:
                previous = current
                current = current.next
        temp = Node(item)
        if previous == None:
            temp.next = self.__head
            self.__head = temp
        else:
            temp.next = current
            previous.next = temp

    def remove(self, item:object) -> None:
        current = self.__head
        previous = None
        found = False
        stop = False
        while not found and not stop:
            if current == item:
                found = True
            elif current.data > item:
                stop = True
            else:
                previous = current
                current = current.next
        if found:
            if previous == None:
                self.__head = current.next
            else:
                previous.next = current.next
        else:
            raise KeyError

    def search(self, item:object) -> bool:
        current = self.__head
        found = False
        stop = False
        while not found and not stop and current != None:
            if current.data == item:
                found = True
            elif current.data > item:
                stop = True
            else:
                current = current.next
        return found

    def isEmpty(self) -> bool:
        return self.__head == None

    def length(self) -> int:
        current = self.__head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def __len__(self) -> int:
        return self.length()
    
    def index(self, item:object) -> int:
        current = self.__head
        found = False
        stop = False
        idx = 0
        while not found and not stop and current != None:
            if current.data == item:
                found = True
            elif current.data > item:
                stop = True
            else:
                current = current.next
        if found:
            return idx
        else:
            raise ValueError

    def pop(self, pos:int = -1) -> object:
        curlen = self.length()
        if pos < 0:
            pos = pos + curlen
        if pos >= 0 and pos < curlen:
            current = self.__head
            previous = None
            while pos != 0:
                previous = current
                current = current.next
                pos -= 1
            if previous == None:
                self.__head = current.next
            else:
                previous.next = current.next
            return current
        else:
            raise IndexError
    
    def __str__(self) -> str:
        res = "["
        if not self.isEmpty():
            res = res + str(self.__head.data)
            current = self.__head.next
            while current != None:
                res = res + ', ' + str(current.data)
                current = current.next
        res = res + ']'
        return res

    def __contains__(self, key:object) -> bool:
        return self.search(key)