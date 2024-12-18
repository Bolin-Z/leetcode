# 题目：150.逆波兰表达式求值
# 标签：栈 数组 数学
# 难度：中等
# 日期：12.18

from typing import *

# 思路:
#

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token in op:
                right_op = stack.pop()
                left_op = stack.pop()
                if token == "+": tmp = left_op + right_op
                elif token == "-": tmp = left_op - right_op
                elif token == "*": tmp = left_op * right_op
                elif token == "/": tmp = int(left_op / right_op) # python 语言特性
                stack.append(tmp)
            else:
                stack.append(int(token))
        return stack[0]

    def test(self):
        """test code
        """
        test_cases = [
            {
                "Input ": [["10","6","9","3","+","-11","*","/","*","17","+","5","+"]],
                "Expect": [],
                "Output": []
            }
        ]
        for i, case in enumerate(test_cases):
            case["Output"].append(self.evalRPN(case["Input "][0])) # 调用求解
            print(f"Test {i + 1}")
            for key, val in case.items():
                print(f"\t\t{key}: {val}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()