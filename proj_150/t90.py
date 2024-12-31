# 题目：130.被围绕的区域
# 标签：BFS DFS 并查集 数组 矩阵
# 难度：中等
# 日期：12.23

from typing import *

# 思路:
# 从四个边界开始 找到不可捕获的区域 标记
# 遍历一次 board 捕获可以捕获的区域

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row_num, col_num = len(board), len(board[0])
        def dfs(i:int, j:int) -> None:
            if i < 0 or i >= row_num or j < 0 or j >= col_num or board[i][j] != "O":
                return
            board[i][j] = "Y"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        for j in range(col_num):
            dfs(0, j)
            dfs(row_num - 1, j)
        for i in range(row_num):
            dfs(i, 0)
            dfs(i, col_num - 1)
        for i in range(row_num):
            for j in range(col_num):
                if board[i][j] == "Y":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

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