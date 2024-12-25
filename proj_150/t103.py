# 题目：77.组合
# 标签：回溯
# 难度：中等
# 日期：12.25

from typing import *
from copy import copy
# 思路:
#

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, selected = [], []
        def dfs(idx:int, last:int) -> None:
            nonlocal selected, ans
            if len(selected) + n - last + 1 < k:
                return
            if idx == k:
                ans.append(selected.copy())
                return
            candidate = [i for i in range(last + 1, n + 1)]
            for num in candidate:
                selected.append(num)
                dfs(idx + 1, num)
                selected.pop()
        dfs(0, 0)
        return ans
    
    def test(self):
        self.combine(4, 2)

# 官方题解
# 考虑第i个位置选或不选
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        selected = []
        ans = []
        def dfs(cur:int) -> None:
            nonlocal n, k, selected, ans
            if len(selected) + (n - cur + 1) < k:
                return
            if len(selected) == k:
                ans.append(selected.copy())
                return
            # 考虑当前位置
            selected.append(cur) # 选
            dfs(cur + 1)
            selected.pop() # 回溯
            dfs(cur + 1) # 不选
        dfs(1)
        return ans

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()