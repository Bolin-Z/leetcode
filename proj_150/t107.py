# 题目：79.单词搜索
# 标签：数组 字符串 回溯 矩阵
# 难度：中等
# 日期：12.26

from typing import *

# 思路:
#

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(idx:int, x:int, y:int) -> bool:
            if idx == len(word):
                return True
            if 0 <= x < m and 0 <= y < n and board[x][y] == word[idx]:
                board[x][y] = "#"
                for nx, ny in [(x + 1, y),(x - 1, y),(x, y + 1), (x, y - 1)]:
                    if dfs(idx + 1, nx, ny):
                        return True
                board[x][y] = word[idx]
            return False
        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        return False



    def test(self):
        board = [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ]
        word = "ABCCED"
        self.exist(board, word)

# 官方题解
# 可以优化的点 word开头字母出现次数为 x，结尾字母出现次数为 y
# 当 y < x 时可以将单词反转(匹配更少次数)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word): # 不满足字符出现数
            return False
        if cnt[word[-1]] < cnt[word[0]]: # 反转
            word = word[::-1]
        m, n = len(board), len(board[0])
        
        def dfs(idx:int, x:int, y:int) -> bool:
            if board[x][y] != word[idx]:
                return False
            if idx == len(word) - 1: # 过了第一个 if 说明字符匹配
                return True
            board[x][y] = "#" # 标记走过
            for nx, ny in (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y):
                if 0 <= nx < m and 0 <= ny < n and dfs(idx + 1, nx, ny):
                    return True
            board[x][y] = word[idx] # 恢复
            return False
        
        return any(dfs(0, i, j) for i in range(m) for j in range(n))

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()