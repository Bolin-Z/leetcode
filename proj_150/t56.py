# 题目：224.基本计算器
# 标签：
# 难度：困难
# 日期：12.18

from typing import *

# 思路:
# 中缀转后缀 再逆波兰？

class Solution:
    def calculate(self, s: str) -> int:
        pass
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