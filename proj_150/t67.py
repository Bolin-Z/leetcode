# 题目：146.LRU缓存
# 标签：
# 难度：中等
# 日期：12.19

from typing import *

# 思路:
#

class LinkNode:
    def __init__(self, val:int=0, next:'Optional[LinkNode]'=None, prev:'Optional[LinkNode]'=None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_num = 0
        self.hash_table = {}
        self.old = self.new = None

    def get(self, key: int) -> int:
        if key in self.hash_table:
            ptr:LinkNode = self.hash_table[key]
            prev = ptr.prev
            next = ptr.next
            prev.next = next
            next.prev = prev
            self.new.next = ptr
            ptr.prev = self.new
            return ptr.val
        return -1

    def put(self, key: int, value: int) -> None:
        pass

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