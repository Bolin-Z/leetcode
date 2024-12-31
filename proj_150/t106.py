# 题目：22.括号生成 *
# 标签：字符串 DP 回溯
# 难度：中等
# 日期：12.26

from typing import *
from functools import lru_cache

# 思路:
#

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []
        def dfs(left:int, right:int) -> None:
            if left == n and right == n:
                ans.append("".join(path))
                return
            if left < n:
                path.append("(")
                dfs(left + 1, right)
                path.pop()
            # if right < n and right + 1 <= left:
            if right < left: # 化简
                path.append(")")
                dfs(left, right + 1)
                path.pop()

        dfs(0, 0)
        return ans

    def test(self):
        self.generateParenthesis(2)

# 官方题解
# 递归：生成的括号数目
class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append(f"({left}){right}") # (a)b a b 为合法括号序列
        return ans
# 由上面的可以有DP
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dp[i] 为生成 i 个括号的所有可能
        dp = [[] for _ in range(n + 1)]
        dp[0].append("")
        for i in range(1, n + 1):
            for j in range(i):
                k = i - 1 - j
                for left in dp[j]:
                    for right in dp[k]:
                        dp[i].append(f"({left}){right}")
        return dp[n]
    def test(self):
        self.generateParenthesis(3)

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()