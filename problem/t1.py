"""sum of two number
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in table:
                return [table[rest], i]
            else:
                table[rest] = i