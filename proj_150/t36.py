# 题目：48.旋转图像
# 标签：数组 数学 矩阵
# 难度：中等
# 日期：12.16

from typing import *

# 思路:
#

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left, top, right, down = 0, 0, n - 1, n - 1
        while n > 1:
            for _ in range(n - 1):
                self.move_one(matrix, left, top, right, down)
            left += 1
            top += 1
            right -= 1
            down -= 1
            n -= 2
    def move_one(self, matrix:List[List[int]], left, top, right, down) -> None:
        temp = matrix[top][left]
        for i in range(top, down):
            matrix[i][left] = matrix[i + 1][left]
        for i in range(left, right):
            matrix[down][i] = matrix[down][i + 1]
        for i in range(down, top, -1):
            matrix[i][right] = matrix[i - 1][right]
        for i in range(right, left, -1):
            matrix[top][i] = matrix[top][i - 1]
        matrix[top][left + 1] = temp

    def test(self):
        """test code
        """
        test_cases = [
            [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
            [[1,2,3],[4,5,6],[7,8,9]]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.rotate(case)
            if type(answer) == List:
                for ans in answer:
                    print(f"\t\t{ans}")
            else:
                print(f"\t\t{answer}")

# 官方题解
# 水平翻转 + 沿对角线对称
# 旋转过后对应的坐标应有
# m[i][j] -> m[j][n - i]
# 水平翻转有
# m[i][j] -> m[n - i][j]
# 轴对称有
# m[i][j] -> m[j][i]
# 复合后有
# m[i][j] -> m[n - i][j] -> m[j][n - i]
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# 原地旋转法
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()