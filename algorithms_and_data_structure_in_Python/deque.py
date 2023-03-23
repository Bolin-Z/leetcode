from typing import Any
class Deque:
    def __init__(self) -> None:
        self.items = []
    
    def isEmpty(self) -> bool:
        return self.items == []
    
    def addFront(self, item:Any) -> None:
        self.items.append(item)
    
    def addRear(self, item:Any) -> None:
        self.items.insert(0, item)
    
    def removeFront(self) -> Any:
        return self.items.pop()
    
    def removeRear(self) -> Any:
        return self.items.pop(0)
    
    def size(self) -> int:
        return len(self.items)
    
    @staticmethod
    def test() -> None:
        d = Deque()
        print(d.isEmpty())
        d.addRear(4)
        d.addRear('dog')
        d.addFront('cat')
        d.addFront(True)
        print(d.size())
        print(d.isEmpty())
        d.addRear(8.4)
        print(d.removeRear())
        print(d.removeFront())

class PalindromeChecker:
    @staticmethod
    def checker(aString:str) -> bool:
        chardeque = Deque()

        for ch in aString:
            chardeque.addRear(ch)
        
        stillEqual = True

        while chardeque.size() > 1 and stillEqual:
            first = chardeque.removeFront()
            last = chardeque.removeRear()
            if first != last:
                stillEqual = False
        
        return stillEqual

if __name__ == "__main__":
    print(PalindromeChecker.checker("toot"))
    print(PalindromeChecker.checker("lsdkjfskf"))