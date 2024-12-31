# 题目：200.岛屿数量
# 标签：BFS DFS 并查集 数组 矩阵
# 难度：中等
# 日期：12.23

from typing import *

# 思路:
# 求解连通的1的块数 每次碰到1做一次 DFS 消除所有 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        def dfs(i:int, j:int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            dfs(i, j - 1)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i + 1, j)
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == '1':
                    dfs(i, j)
                    ans += 1
        return ans

    def test(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        self.numIslands(grid)

# 官方题解
# BFS写法
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "1":
                    ans += 1
                    grid[i][j] == "0"
                    visit_que = deque([(i, j)])
                    while visit_que:
                        r, c = visit_que.popleft()
                        for x, y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                                visit_que.append((x, y))
                                grid[x][y] = "0"
        return ans


# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()