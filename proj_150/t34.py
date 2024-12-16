# 题目：36.有效的数独
# 标签：数组 哈希表 矩阵
# 难度：中等
# 日期：12.16

from typing import *

# 思路:
# 按顺序比较吧

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            check = set()
            for n in board[i]:
                if n in check and n != ".": return False
                else: check.add(n)
        for i in range(len(board)):
            check = set()
            for j in range(9):
                n = board[j][i]
                if n in check and n != ".": return False
                else: check.add(n)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = set()
                for dy in range(3):
                    for dx in range(3):
                        n = board[i + dy][j + dx]
                        if n in check and n != ".": return False
                        else: check.add(n)
        return True

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
# 还可以只遍历一次
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        block = [[set() for i in range(3)] for j in range(3)]
        for y in range(9):
            for x in range(9):
                n = board[y][x]
                if n in rows[y] and n != ".": return False
                else: rows[y].add(n)
                if n in columns[x] and n != ".": return False
                else: columns[x].add(n)
                if n in block[y//3][x//3] and n != ".": return False
                else: block[y//3][x//3].add(n)
        return True


# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()