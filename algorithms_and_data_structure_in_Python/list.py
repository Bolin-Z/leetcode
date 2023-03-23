from typing import Any

class Node:
    def __init__(self, initdata:Any) -> None:
        self.__data = initdata
        self.__next:Node = None
    
    @property
    def data(self) -> Any:
        return self.__data
    
    @data.setter
    def data(self, newData:Any) -> None:
        self.__data = newData
    
    @property
    def next(self) -> Any:
        return self.__next
    
    @next.setter
    def next(self, newnext) -> None:
        self.__next = newnext

class UnorderList:
    def __init__(self) -> None:
        self.head = None

    def isEmpty(self) -> bool:
        return self.head == None
    
    def add(self,item:Any) -> None:
        temp = Node(item)
        temp.next = self.head
        self.head = temp
    
    def length(self) -> int:
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next

        return count
    
    def search(self, item:Any) -> bool:
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next

        return found
    
    def remove(self, item) -> None:
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next
    
    @staticmethod
    def test() -> None:
        ul = UnorderList()
        print(ul.isEmpty())
        ul.add(31)
        ul.add(77)
        ul.add(17)
        ul.add(93)
        ul.add(26)
        ul.add(54)
        print(ul.length())
        print(ul.search(17))
        print(ul.search(27))

class OrderList:
    def __init__(self) -> None:
        self.head = None
    
    def isEmpty(self) -> bool:
        return self.head == None
    
    def add(self, item:Any) -> None:
        current = self.head
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
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def length(self) -> int:
        current  = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next

        return count

    def search(self, item:Any) -> bool:
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.data == item:
                found = True
            else:
                if current.data > item:
                    stop = True
                else:
                    current = current.next

        return found

    def remove(self, item:Any) -> None:
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = previous.next
        
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

if __name__ == "__main__":
    UnorderList.test()