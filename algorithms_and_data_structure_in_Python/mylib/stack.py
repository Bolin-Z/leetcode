"""stack.py stack implement with list

"""
from typing import Generic, TypeVar

__all__ = ['Stack']

VT = TypeVar('VT')
class Stack(Generic[VT]):
    def __init__(self) -> None:
        self.__items : list[VT] = []

    def push(self, item:VT) -> None:
        self.__items.append(item)

    def pop(self) -> VT:
        try:
            return self.__items.pop()
        except IndexError:
            print("ERROR: CAN NOT POP AN EMPTY STACK")

    def peek(self) -> VT:
        try:
            return self.__items[len(self.__items) - 1]
        except IndexError:
            print("ERROR: CAN NOT PEAK AN EMPTY STACK")

    def isEmpty(self) -> bool:
        return self.__items == []

    def size(self) -> int:
        return len(self.__items)

    def __str__(self) -> str:
        return str(self.__items)