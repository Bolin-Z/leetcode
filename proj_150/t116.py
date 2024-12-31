# 题目：162.寻找峰值 *
# 标签：数组 二分
# 难度：中等
# 日期：12.30

from typing import *

# 思路:
#

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 2 # [0, n - 2]
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > nums[mid + 1]:
                right = mid - 1 # 当 ans = mid 为唯一峰值时 left 会不断移动直到 left == right
            else:
                left = mid + 1 # 此时就会进入这一行 mid = left = right => left' = left + 1 = ans
        return left

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
# 数组两端都认为是-∞, 就是说峰值必然存在
# 考虑 nums[i] 和 nums[i+1]
# 如果 i < n - 1 且 nums[i] < nums[i+1] 则 [i+1, n-1]中一定有一个峰值
# 反言之 当 nums[i] >= nums[i+1] 时 [0, i] 中一定有一个峰值

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()