# 题目：909.蛇梯棋
# 标签：BFS 数组 矩阵
# 难度：中等
# 日期：12.24

from typing import *
from collections import deque

# 思路:
# BFS 记录当前的跳数 队列里放每一跳可以到达的点 层序遍历
# 如果格子为 -1 则更新 后面六个格子
# 如果为蛇 则将目标节点加入队列
# 开一个数组记录是否被visited(甚至可以记录跳数)

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self._n = len(board)
        self._board = board
        target = self._n * self._n
        visit_que = [1]
        visited = set([1])
        step = 0
        while visit_que:
            next_step_que = []
            for last_step in visit_que:
                if last_step == target:
                    return step
                for next_step in range(last_step + 1, min(last_step + 6, target) + 1):
                    if next_step not in visited:
                        snake_ladder = self.get(next_step)
                        if snake_ladder != -1 and snake_ladder not in visited:
                            visited.add(next_step)
                            next_step_que.append(snake_ladder)
                        elif snake_ladder == -1:
                            visited.add(next_step)
                            next_step_que.append(next_step)
            step += 1
            visit_que = next_step_que
        return -1

    def get(self, idx:int) -> int:
        row, col = divmod(idx - 1, self._n)
        col = col if row % 2 == 0 else self._n - 1 - col
        row = self._n - 1 - row
        return self._board[row][col]

    def test(self):
        board = [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,35,-1,-1,13,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,15,-1,-1,-1,-1]
        ]
        # board = [[1,1,-1],[1,1,1],[-1,1,1]]
        board = [
            [-1,-1,27,13,-1,25,-1],
            [-1,-1,-1,-1,-1,-1,-1],
            [44,-1,8,-1,-1,2,-1],
            [-1,30,-1,-1,-1,-1,-1],
            [3,-1,20,-1,46,6,-1],
            [-1,-1,-1,-1,-1,-1,29],
            [-1,29,21,33,-1,-1,-1]
        ]
        ans = self.snakesAndLadders(board)

# 官方题解
# BFS 清晰写法
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def id2rc(idx:int) -> Tuple[int, int]:
            r, c = divmod(idx - 1, n)
            if r % 2 == 1:
                c = n - 1 - c
            return n - 1 - r, c
        vis = set()
        q = deque([(1, 0)])
        while q:
            idx, step = q.popleft()
            for idx_nxt in range(idx + 1, min(idx + 6, n * n) + 1):
                x_nxt, y_nxt = id2rc(idx_nxt)
                if board[x_nxt][y_nxt] > 0:
                    idx_nxt = board[x_nxt][y_nxt]
                if idx_nxt == n * n:
                    return step + 1
                if idx_nxt not in vis:
                    vis.add(idx_nxt)
                    q.append((idx_nxt, step + 1))
        return -1

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()