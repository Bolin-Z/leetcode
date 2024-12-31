# 题目：35.搜索插入位置
# 标签：数组 二分
# 难度：简单
# 日期：12.30

from typing import *

# 思路:
# 二分查找

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(left:int, right:int) -> int:
            nonlocal target
            if left > right:
                return left
            if left == right:
                return left if nums[left] >= target else left + 1
            mid = (left + right + 1) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(left, mid - 1)
            else:
                return binarySearch(mid + 1, right)
        return binarySearch(0, len(nums) - 1)

    def test(self):
        nums = [1,3]
        target = 4
        self.searchInsert(nums, target)

# 官方题解
# 考虑插入时,即找到第一个 大于等于 target 的数的下标 如果都小于 target 返回 nums 长度
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pass
    
    # 闭区间写法
    def both_closed(self, nums: List[int], target:int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    # 左闭右开
    def left_closed_right_open(self, nums: List[int], target:int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid # 不同的地方
        return left
    
    # 开区间
    def both_open(self, nums: List[int], target:int) -> int:
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()