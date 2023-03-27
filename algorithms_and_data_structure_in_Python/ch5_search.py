from typing import Any

def sequentialSearch(alist:list, item:Any) -> bool:
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found

def orderedSequentialSearch(alist:list, item:Any) -> bool:
    """
    :param alist: list of comparable items sorted in ascending order
    :param item: target item
    :return: return True if item is in alist, otherwise False
    """
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found

def binarySearch(alist:list, item:Any) -> bool:
    """
    :param alist: list of comparable items sorted in ascending oreder
    :param item: target item
    :return: return True if item is in alist, otherwise return False
    """
    first = 0
    last = len(alist) - 1
    found = False
    # shrink interv [first, ..., last]
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

def binarySearchRecursion(alist:list, item:Any) -> bool:
    """
    :param alist: list of comparable items sorted in ascending oreder
    :param item: target item
    :return: return True if item is in alist, otherwise return False
    """
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearchRecursion(alist[:midpoint], item)
            else:
                return binarySearchRecursion(alist[midpoint + 1:], item)

def binarySearchRecursion2(alist:list, item:Any, left:int, right:int) -> bool:
    """
    :param alist: list of comparable items sorted in ascending oreder
    :param item: target item
    :param left: left most index of searching interval
    :param right: right most index of searching interval but not included 
    :return: return True if item is in alist, otherwise return False
    """
    if right <= left:
        return False
    else:
        midpoint = (left + right) // 2
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearchRecursion2(alist, item, left, midpoint)
            else:
                return binarySearchRecursion2(alist, item, midpoint + 1, right)

def hash(astring:str, tablesize:int) -> int:
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
    return sum % tablesize

def hash2(astring:str, tablesize:int) -> int:
    sum = 0
    for pos in range(len(astring)):
        sum = sum + (pos + 1) * ord(astring[pos])
    return sum % tablesize

class HashTable:
    def __init__(self) -> None:
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def hashfunction(self, key, size):
        return key % size
    
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size
    
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # open addressing
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                self.data[nextslot] = data
    
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data
    
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, item) -> bool:
        return self.get(item) != None

    def __len__(self) -> int:
        return self.size

if __name__ == "__main__":
    H = HashTable()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"
    print(H.slots)
    print(H.data)
    print(H[20])
    print(H[17])
    H[20] = "duck"
    print(H[20])
    print(H.data)
    print(H[99])