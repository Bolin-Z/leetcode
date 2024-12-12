# 题目：169.多数元素
# 标签：数组 哈希表 分治 计数 排序
# 难度：简单

from typing import *
import collections

# 思路:
# 多数元素个数比其他元素多，一换一，最后剩下的就是多数元素

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_idx = 0
        for check_idx in range(1, len(nums)):
            if nums[majority_idx] != nums[check_idx]:
                if check_idx - majority_idx > 1:
                    nums[majority_idx], nums[check_idx] = nums[check_idx], nums[majority_idx]
                majority_idx += 2
        return nums[majority_idx]


# 官方题解

# hash方法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# Boyer-Moore 投票算法
# 把众数记为 +1 其他数记为 -1 全部加起来显然和大于 0
# 维护一个候选众数 candidate 和出现的次数 count
# 初始时 candidate 为任意值 count = 0
# 遍历每个 x 如果 count == 0 设置 x 为 candidate
# 如果 x == candidate count的数目 + 1 否则 - 1

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)   
        return candidate