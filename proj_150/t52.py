# 题目：20. 有效的括号
# 标签：栈 字符串
# 难度：简单
# 日期：12.18

from typing import *
from collections import deque
from math import inf

# 思路:
# 维护一个栈，如果遇到左括号就add，右括号就pop栈并比较

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: # 数目不匹配
            return False
        ptype = {"(":1,")":-1,"{":2,"}":-2,"[":3,"]":-3}
        stack = deque()
        stack.append(inf)
        for c in s:
            if ptype[c] > 0: stack.append(ptype[c]) # 左括号
            elif stack.pop() + ptype[c] != 0:
                return False
        return len(stack) == 1


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