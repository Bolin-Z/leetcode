# 题目：380. O(1)时间插入、删除和获取随机元素
# 标签：设计 数组 哈希表 数学 随机化
# 难度：中等

from typing import *
from random import *

# 思路:
# 哈希表 + 变长数组
# python里字典
# 数据结构题

# class Solution:
#     def test(self):
#         """test code
#         """
#         test_cases = []
#         pass

class RandomizedSet:

    def __init__(self):
        self.container = []
        self.hash_table = {}

    def insert(self, val: int) -> bool:
        if val in self.hash_table:
            return False
        self.hash_table[val] = len(self.container)
        self.container.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_table:
            return False
        self.container[self.hash_table[val]] = self.container[-1]
        self.hash_table[self.container[-1]] = self.hash_table[val]
        self.container.pop()
        self.hash_table.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.container)

        

# 官方题解

# 测试
# if __name__ == "__main__":
#     solver = Solution()
#     solver.test()