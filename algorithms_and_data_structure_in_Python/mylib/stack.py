"""stack.py stack implement with list

"""
__all__ = ['Stack']

class Stack:
    def __init__(self) -> None:
        self.__items = []

    def push(self, item:object) -> None:
        self.__items.append(item)

    def pop(self) -> object:
        try:
            return self.__items.pop()
        except IndexError:
            print("ERROR: CAN NOT POP AN EMPTY STACK")

    def peek(self) -> object:
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