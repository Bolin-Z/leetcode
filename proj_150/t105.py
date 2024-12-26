# 题目：39.组合总和 *
# 标签：数组 回溯
# 难度：中等
# 日期：12.26

from typing import *

# 思路:
# 回溯 具体思路如代码

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, selected, n = [], [], len(candidates)
        candidates.sort() # 保证升序排序
        def dfs(idx:int, res:int) -> None:
            nonlocal ans, selected, n
            if res == 0:
                ans.append(selected.copy())
                return
            if idx >= n or res < candidates[idx]: # 因为保证了升序 后面不可能再有选择
                return
            num = candidates[idx]
            max_num = res // num # 最多可以选择该元素的个数
            for i in range(1, max_num + 1): # 选择 [1, max_num] 个 candidates[idx]
                selected.append(num) # 每次多加一个
                dfs(idx + 1, res - i * num)
            for _ in range(max_num): # 不选择 candidates[idx]
                selected.pop()
            dfs(idx + 1, res)
        dfs(0, target)
        return ans

    def test(self):
        candidates = [2,3,6,7]
        target = 7
        ans = self.combinationSum(candidates, target)

# 官方题解

# 选或不选
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # 保证升序
        ans = []
        path = []

        def dfs(idx:int, res:int) -> None:
            if res == 0: # 找到一个组合
                ans.append(path.copy())
                return
            if idx == len(candidates) or res < candidates[idx]: # 剪枝，没有可以选择的
                return
            # 不选
            dfs(idx + 1, res) 
            # 选
            path.append(candidates[idx])
            dfs(idx, res - candidates[idx]) # 递归到 idx 表示可以重复选取
            path.pop() # 恢复现场
        dfs(0, target)
        return ans

# 枚举选哪个
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        def dfs(idx:int, res:int) -> None:
            if res == 0:
                ans.append(path.copy())
                return
            if res < candidates[idx]: # 选不了，剪枝
                return
            for j in range(idx, len(candidates)): # 从 candidates[idx] - candidates[n-1] 中选一个
                path.append(candidates[j])
                dfs(j, res - candidates[j])
                path.pop()
        dfs(0, target)
        return ans

# 完全背包做法
# f[i+1][j] 表示 下标在 [0,i] 中的candidates元素之和是否能为j
# f[i][j] 成立时 f[i + 1][j] 成立
# f[i + 1][j - x] 成立时 f[i + 1][j] 成立 因为多加一个 x 即可
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        f = [[False] * (target + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i, x in enumerate(candidates):
            for j in range(target + 1):
                f[i + 1][j] = f[i][j] or j >= x and f[i + 1][j - x]
        
        ans = []
        path = []

        def dfs(idx:int, res:int) -> None:
            if res == 0:
                ans.append(path.copy())
                return
            if res < 0 or not f[idx + 1][res]: # 无法用下标在[0,idx]中的数字组合出 res
                return
            # 不选
            dfs(idx - 1, res)
            # 选
            path.append(candidates[idx])
            dfs(idx, res - candidates[idx])
            path.pop()
        
        dfs(n - 1, target) # 倒着递归
        return ans

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()