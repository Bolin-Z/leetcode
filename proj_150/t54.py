# 题目：155.最小栈
# 标签：栈 设计
# 难度：中等
# 日期：12.18

from typing import *
from math import inf

# 思路:
# 由于栈的性质，可以为每一个元素维护一个额外的量：该元素加入后整个栈的最小值

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append([val, min(val, self.stack[-1][1])])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]

# 不使用额外空间的做法，栈里保存与当前最小值的差值
# 入栈后再更新最小值
# diff = x - last_min_x

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = -1

    def push(self, val: int) -> None:
        if self.stack:
            diff = val - self.min_value
            self.stack.append(diff)
            self.min_value = min(self.min_value, val)
        else:
            self.stack.append(0)
            self.min_value = val

    def pop(self) -> None:
        # 维护 self.min_value
        diff = self.stack.pop()
        if diff < 0: # self.min_value 为 top 的值
            self.min_value = self.min_value - diff

    def top(self) -> int:
        if self.stack[-1] < 0: # 栈顶为当前最小
            return self.min_value
        else: # 栈顶不为最小
            return self.min_value + self.stack[-1]

    def getMin(self) -> int:
        return self.min_value

# class Solution:
#     def test(self):
#         """test code
#         """
#         test_cases = [
#             {
#                 "Input ": [],
#                 "Expect": [],
#                 "Output": []
#             }
#         ]
#         for i, case in enumerate(test_cases):
#             case["Output"].append(case["Input "]) # 调用求解
#             print(f"Test {i + 1}")
#             for key, val in case.items():
#                 print(f"\t\t{key}: {val}")

# 官方题解

# 测试
if __name__ == "__main__":
    # solver = Solution()
    # solver.test()
    pass