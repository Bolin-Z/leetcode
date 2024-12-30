# 题目：74.搜索二维矩阵
# 标签：数组 二分查找 矩阵
# 难度：中等
# 日期：12.30

from typing import *

# 思路:
# 先纵向二分 再横向二分

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) >> 1
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        search_col = right
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) >> 1
            if matrix[search_col][mid] == target:
                return True
            elif matrix[search_col][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


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
# 排除法 每次比较右上角元素
# 如果等于就是找到
# 如果小于说明当前第一排都小于目标，删除
# 如果大于说明当前最后一列都大于目标，删除
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False

# 一次二分
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) >> 1
            x = matrix[mid // n][mid % n]
            if x == target:
                return True
            elif x < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()