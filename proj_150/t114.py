# 题目：918.环形子数组的最大和
# 标签：动态规划 分治 数组 队列 单调队列
# 难度：中等
# 日期：12.29

from typing import *
from math import *

# 思路:
# 最大子数组和可能在中间 或者 横跨边界
# 对于横跨边界的可以考虑反向, 计算最小子数组和 

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 在中间的情况
        maxSum, minSum, totalSum = -inf, inf, 0
        dp_max, dp_min = -inf, inf
        for n in nums:
            # 更新数组和
            totalSum += n
            # 更新最大子数组
            dp_max = max(dp_max + n, n)
            maxSum = max(maxSum, dp_max)
            # 更新最小子数组
            dp_min = min(dp_min + n, n)
            minSum = min(minSum, dp_min)
        return maxSum if minSum == totalSum else max(maxSum, totalSum - minSum)


    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        pass
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