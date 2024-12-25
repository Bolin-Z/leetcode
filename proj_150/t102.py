# 题目：17.电话号码的字母组合
# 标签：哈希 字符串 回溯
# 难度：中等
# 日期：12.25

from typing import *
from collections import *

# 思路:
# 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        dig2ch = {
            "2":"abc","3":"def","4":"ghi","5":"jkl",
            "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }
        stack = deque()
        n = len(digits)
        ans = []
        def dfs(idx:int) -> None:
            nonlocal digits, n, ans
            if idx < n:
                chs = dig2ch[digits[idx]]
                for c in chs:
                    stack.append(c)
                    dfs(idx + 1)
                    stack.pop()
            else:
                ans.append("".join(stack))
        dfs(0)
        return ans
            
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