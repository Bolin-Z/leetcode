# 题目：146.LRU缓存
# 标签：
# 难度：中等
# 日期：12.19

from typing import *

# 思路:
#

class LinkNode:
    __slots__ = "key", "val", "prev", "next"
    def __init__(self, key:int=0, val:int=0, prev:'Optional[LinkNode]'=None, next:'Optional[LinkNode]'=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = dict()
        self.dummy = LinkNode()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def get(self, key: int) -> int:
        ptr = self.__get_node(key)
        return ptr.val if ptr else -1

    def put(self, key: int, value: int) -> None:
        ptr = self.__get_node(key)
        if ptr is None:
            ptr = LinkNode(key=key, val=value)
            self.__insert_front(ptr)
            self.key_to_node[key] = ptr

            if len(self.key_to_node) > self.capacity:
                oldest = self.dummy.prev
                self.__remove_node(oldest)
                del self.key_to_node[oldest.key]
        ptr.val = value
    
    def __get_node(self, key:int) -> Optional[LinkNode]:
        ptr = None
        if key in self.key_to_node:
            ptr = self.key_to_node[key]
            self.__remove_node(ptr)
            self.__insert_front(ptr)
        return ptr

    def __remove_node(self, n:LinkNode) -> None:
        prev, next = n.prev, n.next
        prev.next = next
        next.prev = prev

    def __insert_front(self, n:LinkNode) -> None:
        n.next = self.dummy.next
        n.prev = self.dummy
        self.dummy.next.prev = n
        self.dummy.next = n

class Solution:
    def test(self):
        """test code
        """
        test_cases = [
            {
                "Input ": [],
                "Expect": [],
                "Output": []
            }
        ]
        for i, case in enumerate(test_cases):
            case["Output"].append(case["Input "]) # 调用求解
            print(f"Test {i + 1}")
            for key, val in case.items():
                print(f"\t\t{key}: {val}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()