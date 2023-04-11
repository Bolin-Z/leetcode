from typing import TypeVar, Generic
from mylib.tools import DEBUG
import random

VT = TypeVar("VT")

class ArrayList(Generic[VT]):
    def __init__(self) -> None:
        self.sizeExponent = 0
        self.maxSize = 0
        self.lastIndex = 0
        self.myArray : list[VT] = []
    
    def append(self, val : VT):
        if self.lastIndex > self.maxSize -  1:
            self.__resize()
        self.myArray[self.lastIndex] = val
        self.lastIndex += 1
    
    def insert(self, idx:int, val:VT) -> None:
        if self.lastIndex > self.maxSize - 1:
            self.__resize()
        for i in range(self.lastIndex, idx - 1, -1):
            self.myArray[i + 1] = self.myArray[i]
        self.lastIndex += 1
        self.myArray[idx] = val

    def __resize(self):
        newsize = 2 ** self.sizeExponent
        DEBUG.PRINT("newsize = ", newsize)
        newarray : list[VT] = [0] * newsize
        for i in range(self.maxSize):
            newarray[i] = self.myArray[i]
        self.maxSize = newsize
        self.myArray = newarray
        self.sizeExponent += 1
    
    def __getitem__(self, idx:int) -> VT:
        if idx < self.lastIndex:
            return self.myArray[idx]
        else:
            raise LookupError("index out of bounds")
        
    def __setitem__(self, idx:int, val:VT) -> None:
        if idx < self.lastIndex:
            self.myArray[idx] = val
        else:
            raise LookupError("index out of bounds")
    
def modexp(x, n, p):
    if n == 0:
        return 1
    t = (x * x) % p
    tmp = modexp(t, n//2, p)
    if n%2 != 0:
        tmp = (tmp * x) % p
    return tmp

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def ext_gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = ext_gcd(y, x%y)
        return (d, b, a-(x//y)*b)

def RSAgenKeys(p, q):
    n = p * q
    pqminus = (p - 1) * (q - 1)
    e = int(random.random() * n)
    while gcd(pqminus, e) != 1:
        e = int(random.random() * n)
    d, a, b = ext_gcd(pqminus, e)
    if b < 0:
        d = pqminus + b
    else:
        d = b
    return ((e, d, n))

def RSAencrypt(m, e, n:int):
    chunks = toChunks(m, n.bit_length() // 8 * 2)
    encList = []
    for messChunk in chunks:
        c = modexp(messChunk, e, n)
        encList.append(c)
    return encList

def RSAdecrypt(chunkList, d, n:int):
    rList = []
    for c in chunkList:
        m = modexp(c, d, n)
        rList.append(m)
    return chunksToPlain(rList, n.bit_length() // 8 * 2)

def toChunks(m, chunkSize):
    byteMess = bytes(m, 'utf-8')
    hexString = ''
    for b in byteMess:
        hexString = hexString + ("%02x" % b)
    
    numChunks = len(hexString) // chunkSize
    chunkList = []
    for i in range(0, numChunks * chunkSize + 1, chunkSize):
        chunkList.append(hexString[i:i+chunkSize])
    chunkList = [eval('0x' + x) for x in chunkList if x]
    return chunkList

def chunksToPlain(clist, chunkSize):
    hexList = []
    for c in clist:
        hexSting = hex(c)[2:]
        clen = len(hexSting)
        hexList.append('0'*((chunkSize - clen) % 2) + hexSting)
    hstring = "".join(hexList)
    messArray = bytearray.fromhex(hstring)
    return messArray.decode('utf-8')

def simpleMatcher(pattern : str, text : str) -> int:
    starti = 0
    i = 0
    j = 0
    match = False
    stop = False
    while not match and not stop:
        if text[i] == pattern[j]:
            i = i + 1
            j = j + 1
        else:
            starti = starti + 1
            i = starti
            j = 0
        
        if j == len(pattern):
            match = True
        else:
            if i == len(text):
                stop = True
    if match:
        return i - j
    else:
        return - 1

def mismatchLinks(pattern : str) -> dict[int, int]:
    augPattern = "0" + pattern
    links = {}
    links[1] = 0
    for k in range(2, len(augPattern)):
        s = links[k - 1]
        stop = False
        while s >= 1 and not stop:
            if augPattern[s] == augPattern[k - 1]:
                stop = True
            else:
                s = links[s]
        links[k] = s + 1
    return links