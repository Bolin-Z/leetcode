# 题目：189.轮转数组
# 标签：数组 数学 双指针
# 难度：中等

from typing import *

# 思路:
# 翻转法：
# 先将整个数组反转一次
# 然后分别将 [0, k mod n - 1] 与 [k mod n , n - 1] 区间内的元素反转即可

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums: List[int], start:int, end:int) -> None:
            """reverse nums[start, end]
            """
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        n = len(nums)
        k %= n 
        if k != 0:
            reverse(nums, 0, n - 1)
            reverse(nums, 0, k - 1)
            reverse(nums, k, n - 1)

# 官方题解