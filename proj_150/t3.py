# 题目：26. 删除有序数组中的重复项
# 标签：数组 双指针
# 难度：easy

from typing import *

# 思路:
# 一个指针维护以及整理好的数组，因为非严格递增，移动另一根指针，找到可以下一个可以插入的元素就好

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tail_ptr = 0
        # check_ptr = 1
        # while check_ptr < len(nums):
        for check_ptr in range(1, len(nums)): # 用 for 会快，可能省去了每次len？还是别的？
            if nums[check_ptr] != nums[tail_ptr]:
                tail_ptr += 1
                # 可以优化的地方：当 check_ptr > tail_ptr + 1 才进行复制
                if check_ptr > tail_ptr:
                    nums[tail_ptr] = nums[check_ptr]
            check_ptr += 1
        return tail_ptr + 1


# 官方题解
# 略