# 题目：153.寻找旋转排序数组中的最小值
# 标签：数组 二分查找
# 难度：中等
# 日期：12.30

from typing import *

# 思路:
# 二分查找，将mid与数组最后一个比较

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 2
        while left <= right:
            # 循环不变式
            # right + 1 为最小值及其右侧位置
            # left - 1 为最小值左侧位置
            mid = (left + right) >> 1
            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]

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