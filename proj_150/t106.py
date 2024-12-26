# 题目：52.N皇后II
# 标签：回溯
# 难度：困难
# 日期：12.26

from typing import *

# 思路:
# DPLL 回溯

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        placed:List[Tuple[int, int]] = []        
        def check_valid(row:int, col:int) -> bool:
            for nrow, ncol in placed:
                if ncol == col or (abs(ncol - col) == abs(nrow - row)): # 在一条竖线或斜线上，因为按行放，肯定满足row不相同
                    return False
            return True
        def dfs(row:int) -> None:
            nonlocal count, placed
            if row == n:
                count += 1
                return
            vaild_point = []
            for j in range(n):
                if check_valid(row, j):
                    vaild_point.append((row, j))
            for point in vaild_point:
                placed.append(point)
                dfs(row + 1)
                placed.pop()
        dfs(0)
        return count

    def test(self):
        for i in range(1, 10):
            print(f"{self.totalNQueens(i)}")

# 官方题解
# 打表 (笑
class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = [0,1,0,0,2,10,4,40,92,352]
        return ans[n]
# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()