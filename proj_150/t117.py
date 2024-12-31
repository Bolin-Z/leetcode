# 题目：33.搜索旋转排序数组 *
# 标签：
# 难度：中等
# 日期：12.30

from typing import *

# 思路:
# 先找出首元素所在的位置 然后分成两个部分查找？

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 2 # 关键 当长度为1时，-2 可以直接跳出循环
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] < nums[-1]: # 比较的数！
                right = mid - 1
            else:
                left = mid + 1
        head_pos = left
        if target <= nums[-1]:
            left, right = head_pos, len(nums) - 1
        else:
            left, right = 0, head_pos - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] < target: # 先判断左区间变动条件
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def test(self):
        nums = [1]
        target = 1
        self.search(nums, target)

# 官方题解
# 二分查找的循环不变量
# 一次二分
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 蓝色区域为target及target右侧 红色区域为target左侧
        def is_blue(i: int) -> bool:
            end = nums[-1]
            if nums[i] > end: # 中点大于最后一个数 则必定为两段升的情况
                return target > end and nums[i] >= target # 此时当 target 与 nums[i] 在同一段且 nums[i] >= target 时 nums[i]及其右侧染蓝色
            else: 
                # 中点小于最后一个数 有两种情况
                # target 与 nums[i] 落在不同段，即 target > end 此时 nums[i] 也染蓝
                # target 与 nums[i] 落在同一段升，此时有 nums[i] >= target 时染蓝
                return target > end or nums[i] >= target
        left, right = 0, len(nums) - 2 # nums[n-1]一定是蓝色的，因为其一定在target及其左侧。target 为最后一个时也成立
        while left <= right: # 有元素存在
            # 循环不变式 
            # right + 1 及之后一定是蓝色
            # left - 1 及之后一定是红色
            # mid = (left + right) >> 1
            mid = left + (right - left) // 2 # 防止溢出写法
            if is_blue(mid):
                right = mid - 1
            else:
                left = mid + 1
        return right + 1 if nums[right + 1] == target else -1

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()