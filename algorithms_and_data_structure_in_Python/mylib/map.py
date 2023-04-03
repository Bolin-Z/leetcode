"""map.py mapping data structure
"""
from abc import ABC, abstractmethod

__all__ = ["HashTable", "Map"]

class Map(ABC):
    """
    Map interface
    """
    @abstractmethod
    def put(self, key:object, val:object) -> None:
        pass

    @abstractmethod
    def get(self, key:object) -> object | None:
        pass

    @abstractmethod
    def remove(self, key:object) -> None:
        pass

    def __getitem__(self, key:object) -> object | None:
        return self.get(key)

    def __setitem__(self, key:object, data:object) -> None:
        self.put(key, data)

    def __delitem__(self, key:object) -> None:
        self.remove(key)

    def __contains__(self, key:object) -> bool:
        return self.get(key) != None

    @abstractmethod
    def len(self) -> int:
        pass

    def __len__(self) -> int:
        return self.len()

class HashTable(Map):
    EXTENDBOUND = 0.75
    SHRINKBOUND = 0.1
    MINSIZE = 11
    def __init__(self) -> None:
        super().__init__()
        self.__size:int = HashTable.MINSIZE
        self.__loaded:int = 0
        self.__slots:list[int] = [None] * self.__size
        self.__data:list[object] = [None] * self.__size
    
    def __hashfunction(self, key:int):
        return key % self.__size
    
    def __rehash(self, oldhash:int):
        return (oldhash + 1) % self.__size
    
    def __extend(self):
        self.__changesize(self.__size * 2 + 1)
    
    def __shrink(self):
        self.__changesize(max(HashTable.MINSIZE, self.__size // 2))
    
    def __changesize(self, newsize:int):
        oldsize = self.__size
        self.__size = newsize
        newslots = [None] * self.__size
        newdata = [None] * self.__size

        for i in range(oldsize):
            if self.__slots[i] != None:
                key = self.__slots[i]
                val = self.__data[i]
                hashval = self.__hashfunction(key)
                while newslots[hashval] != None:
                    hashval = self.__rehash(hashval)
                newslots[hashval] = key
                newdata[hashval] = val

        self.__slots = newslots
        self.__data = newdata
    
    def put(self, key: object, val: object) -> None:
        if (self.__loaded / self.__size) > HashTable.EXTENDBOUND:
            self.__extend()
        
        hashvalue = self.__hashfunction(key)

        if self.__slots[hashvalue] == None:
            self.__slots[hashvalue] = key
            self.__data[hashvalue] = val
            self.__loaded = self.__loaded + 1
        else:
            # open addressing
            if self.__slots[hashvalue] == key:
                # replace old value with new value
                self.__data[hashvalue] = val
            else:
                nextslot = self.__rehash(hashvalue)
                while self.__slots[nextslot] != None and self.__slots[nextslot] != key:
                    nextslot = self.__rehash(nextslot)
                if self.__slots[nextslot] == None:
                    self.__slots[nextslot] = key
                    self.__loaded = self.__loaded + 1
                self.__data[nextslot] = val

    def get(self, key: object) -> object | None:
        startslot = self.__hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        while self.__slots[position] != None and not found and not stop:
            if self.__slots[position] == key:
                found = True
                data = self.__data[position]
            else:
                position = self.__rehash(position)
                if position == startslot:
                    stop = True
        return data
    
    def remove(self, key: object) -> None:
        startslot = self.__hashfunction(key)
        stop = False
        found = False
        position = startslot
        while self.__slots[position] != None and not found and not stop:
            if self.__slots[position] == key:
                found = True
            else:
                position = self.__rehash(position)
                if position == startslot:
                    stop = True
        if found:
            self.__slots[position] = None
            self.__data[position] = None
            self.__loaded -= 1
            if (self.__loaded / self.__size) < HashTable.SHRINKBOUND and self.__size > HashTable.MINSIZE:
                self.__shrink()
        else:
            raise KeyError
    
    def len(self) -> int:
        return self.__loaded

if __name__ == "__main__":
    pass