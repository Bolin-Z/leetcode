# 题目：73.矩阵置零
# 标签：数组 哈希表 矩阵
# 难度：中等
# 日期：12.16

from typing import *

# 思路:
# 用每行和每列的第一个来标记该行/列是否要全部置0
# 第0行和第0列用额外两个变量

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rf, cf = False, False
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            if matrix[0][i] == 0:
                rf = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                cf = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0
        if rf:
            for j in range(n):
                matrix[0][j] = 0
        if cf:
            for i in range(m):
                matrix[i][0] = 0

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