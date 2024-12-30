# 题目：34.在排序数组中查找元素的第一个和最后一个位置
# 标签：
# 难度：中等
# 日期：12.30

from typing import *

# 思路:
# 找到第一个小于target的数和第一个大于target的数的位置

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_min() -> int:
            # 找到第一个小于target的位置
            left, right = 0, len(nums) - 1
            while left <= right: # 确保有元素
                # 循环不变式
                # right + 1 及之后为大于等于 target 的
                # left - 1 及之前为小于 target 的位置
                mid = (left + right) >> 1
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        def find_max() -> int:
            # 找到第一个大于target的位置
            left, right = 0, len(nums) - 1
            while left <= right: # 确保有元素
                # 循环不变式
                # right + 1 及之后为大于 target 的
                # left - 1 及之前为小于等于 target 的
                mid = (left + right) >> 1
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        min_idx = find_min()
        max_idx = find_max()
        first_idx = min_idx + 1 if min_idx + 1 < len(nums) and nums[min_idx + 1] == target else -1
        last_idx = max_idx - 1 if max_idx - 1 > -1 and nums[max_idx - 1] == target else -1
        return [first_idx, last_idx]


    def test(self):
        nums = [5,7,7,8,8,10]
        target = 8
        self.searchRange(nums, target)

# 官方题解
# 代码重用 不用分别写两个
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(t:int) -> int:
            # 返回 nums[i] >= t 的最小下标 i
            left, right = 0, len(nums) - 1
            while left <= right: # 保证元素存在
                # 循环不变式
                # right + 1 为 >= target的
                # left - 1 为 < target的
                mid = (left + right) >> 1
                if nums[mid] < t:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        start = lower_bound(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1] # 不存在
        end = lower_bound(target + 1) - 1 # 找到 >= target + 1 的最小下标 则该下标 - 1 即为最后一个target
        return [start, end]
            

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()