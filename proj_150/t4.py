# 题目：80. 删除有序数组重复项 II
# 标签：数组 双指针
# 难度：中等

from typing import *

# 思路:
# 使用三个指针？head tail 之间保留重复的数字
# 其实复杂了，因为必定保证连续

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        max_length = 2
        head_ptr = 0
        tail_ptr = 0
        for check_ptr in range(1, len(nums)):
            if nums[check_ptr] != nums[tail_ptr]:
                tail_ptr += 1
                head_ptr = tail_ptr
                if check_ptr > tail_ptr:
                    nums[tail_ptr] = nums[check_ptr]
            else:
                if tail_ptr - head_ptr + 1 < max_length:
                    tail_ptr += 1
                    if check_ptr > tail_ptr:
                        nums[tail_ptr] = nums[check_ptr]
            check_ptr += 1
        del nums[1]
        return tail_ptr + 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def solve(k:int):
            # k is the max length
            tail_ptr = 0
            for x in nums:
                if tail_ptr < k or nums[tail_ptr - k] != x:
                    # 对应于数组长度小与 k 的时候
                    # 大于k的时候
                    nums[tail_ptr] = x
                    tail_ptr += 1
            return tail_ptr
        return solve(2)


# 官方题解

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         def solve(k):
#             u = 0
#             for x in nums:
#                 if u < k or nums[u - k] != x:
#                     nums[u] = x
#                     u += 1
#             return u
#         return solve(2)
