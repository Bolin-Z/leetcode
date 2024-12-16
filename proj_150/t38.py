# 题目：289.生命游戏
# 标签：数组 矩阵 模拟
# 难度：中等
# 日期：12.16

from typing import *

# 思路:
# 每个格子有四种状态 (0, 0) (0, 1) (1, 0) (1, 1)

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        DEAD, LIVE = int(0), int(1)
        STATE_1, STATE_2, STATE_3, STATE_4 = int(2), int(3), int(4), int(5)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                alive_cnt = - board[i][j]
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        x, y = i + dx, j + dy
                        if 0 <= x and x < m and 0 <= y and y < n:
                            if board[x][y] == LIVE or board[x][y] == STATE_3 or board[x][y] == STATE_4:
                                alive_cnt += 1
                if board[i][j] == DEAD:
                    if alive_cnt == 3:
                        board[i][j] = STATE_2
                    else:
                        board[i][j] = STATE_1
                else:
                    if alive_cnt < 2 or alive_cnt > 3:
                        board[i][j] = STATE_3
                    else:
                        board[i][j] = STATE_4
        for i in range(m):
            for j in range(n):
                state = board[i][j]
                if state == STATE_1 or state == STATE_3:
                    board[i][j] = 0
                else:
                    board[i][j] = 1
    
    def test(self):
        """test code
        """
        test_cases = []
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = []
            if type(answer) == List:
                for ans in answer:
                    print(f"\t\t{ans}")
            else:
                print(f"\t\t{answer}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()