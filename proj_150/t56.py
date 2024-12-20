# 题目：224.基本计算器 ## 多理解
# 标签：栈 递归 数学 字符串
# 难度：困难
# 日期：12.18

from typing import *

# 思路:
# 中缀转后缀 再逆波兰?
# 用两个栈实现：操作数栈和操作符栈
# 遇到操作数就压栈 遇到操作符进行相关操作

class Solution:
    def calculate(self, s: str) -> int:
        operand, op = [], []
        idx, n = 0, len(s)

        def calc():
            operator = op.pop()
            roperand = operand.pop()
            loperand = operand.pop()
            if operator == "+": operand.append(loperand + roperand)
            elif operator == "-": operand.append(loperand - roperand)

        while idx < n:
            if s[idx] == " ":
                pass
            elif s[idx] == "+":
                while op and op[-1] != "(":
                    calc()
                op.append("+")
            elif s[idx] == "-":
                if not operand or operand[-1] == "(":
                    operand.append(0)
                while op and op[-1] != "(":
                    calc()
                op.append("-")
            elif s[idx] == "(":
                operand.append("(")
                op.append("(")
            elif s[idx] == ")":
                while op[-1] != "(":
                    calc()
                op.pop()
                exp = operand.pop()
                operand.pop() # "("
                operand.append(exp)
            else: # get a number
                num = int(s[idx])
                while idx < n - 1 and s[idx + 1] not in {" ", "+", "-", "(", ")"}:
                    num = num * 10 + int(s[idx + 1])
                    idx += 1
                operand.append(num)
            idx += 1
        while op:
            calc()
        return operand[-1]

    def test(self):
        """test code
        """
        test_cases = [
            {
                "Input ": ["1 + 1"],
                "Expect": [],
                "Output": []
            },
            {
                "Input ": ["(1+(4+5+2)-3)+(6+8)"],
                "Expect": [],
                "Output": []
            },
            {
                "Input ": ["1-(-2)"],
                "Expect": [],
                "Output": []
            },
            {
                "Input ": ["-2+(-3)"],
                "Expect": [],
                "Output": []
            }
        ]
        for i, case in enumerate(test_cases):
            case["Output"].append(self.calculate(case["Input "][0])) # 调用求解
            print(f"Test {i + 1}")
            for key, val in case.items():
                print(f"\t\t{key}: {val}")

# 官方题解
# 使用拆括号的方式 遇到括号记录正负 维护一个正负变量

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()