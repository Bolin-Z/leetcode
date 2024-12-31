# 题目：53.最大子数组和
# 标签：数组 分治 动态规划
# 难度：中等
# 日期：12.27

from typing import *
from math import *

# 思路:
# 动态规划
# dp[j] 以第j个结尾的最大和连续子数组
# dp[j] = max(dp[j - 1] + nums[j], nums[j])

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxSum = -inf
#         dpj = -inf
#         for n in nums:
#             dpj = max(dpj + n, n)
#             if dpj > maxSum:
#                 maxSum = dpj
#         return maxSum

#     def test(self):
#         """test code
#         """
#         test_cases = [
#             {
#                 "Input ": [],
#                 "Expect": [],
#                 "Output": []
#             }
#         ]
#         for i, case in enumerate(test_cases):
#             case["Output"].append(case["Input "]) # 调用求解
#             print(f"Test {i + 1}")
#             for key, val in case.items():
#                 print(f"\t\t{key}: {val}")

# 官方题解
# 分治法 (线段树?)
# 考虑分成左右两个区间, 最大子数组和有三种情况
#   1. 左子区间最大子数组和
#   2. 右子区间最大子数组和
#   3. 横跨左右两个区间: 以左子区间右端为端点的最大子数组和+以右子区间左端为端点的最大子数组和
# 递归边界条件，区间中只有一个元素
class Status:
    __slots__ = 'lSum', 'rSum', 'mSum', 'iSum'
    def __init__(self, lSum:int=0, rSum:int=0, mSum:int=0, iSum:int=0) -> None:
        self.lSum = lSum
        self.rSum = rSum
        self.mSum = mSum
        self.iSum = iSum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def getInfo(l:int, r:int) -> Status:
            nonlocal nums
            if l == r:
                return Status(nums[l], nums[l], nums[l], nums[l])
            mid = (l + r) >> 1
            lSub = getInfo(l, mid)
            rSub = getInfo(mid + 1, r)
            return pushUp(lSub, rSub)

        def pushUp(l:Status, r:Status) -> Status:
            res = Status()
            res.iSum = l.iSum + r.iSum # 区间总和 = 左子区间总和 + 右子区间总和
            res.lSum = max(l.lSum, l.iSum + r.lSum) # 左端开始最大值 = max(左子区间左端开始最大值, 左子区间总和 + 右子区间左端点开始最大值)
            res.rSum = max(r.rSum, r.iSum + l.rSum)
            res.mSum = max(max(l.mSum, r.mSum), l.rSum + r.lSum) # 最大值要不在左/右子区间，要不横跨两个区间
            return res

        res = getInfo(0, len(nums) - 1)
        return res.mSum

    def test(self):
        self.maxSubArray([])

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()