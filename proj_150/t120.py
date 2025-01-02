# 题目：4.寻找两个升序数组的中位数 **
# 标签：数组 二分 分治
# 难度：困难
# 日期：12.31

from typing import *

# 思路:
# 两个有序数组的所有数落在区间 [min(nums1[0],nums2[0]), max(nums1[m - 1], nums2[n - 1])] 之间
# 行不通

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def less_than(nums: List[int], target:int) -> int:
            # 返回 nums[j] < target 的最大下标
            left, right = 0, len(nums) - 1
            while left <= right: # 有元素
                # 循环不变式
                # right + 1 >= target
                # left - 1 < target
                mid = (left + right) >> 1
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right # right + 1 >= target 则 right (left - 1) 为小于 target 的最大下标
        m, n = len(nums1), len(nums2)
        if m == 0:
            return nums2[n//2] / 1 if n%2 == 1 else (nums2[n//2]+nums2[n//2-1]) / 2
        if n == 0:
            return nums1[m//2] / 1 if m%2 == 1 else (nums1[m//2]+nums1[m//2-1]) / 2
        
        long_nums, short_nums = nums1, nums2
        if n > m:
            m, n = n, m
            long_nums, short_nums = short_nums, long_nums
        less_count = (m + n) // 2
        long_idx = less_than(long_nums, short_nums[-1])


    def test(self):
        nums1 = []
        nums2 = [3]
        self.findMedianSortedArrays(nums1, nums2)

# 官方题解
# 双指针做法
# 中位数可以将数字均匀分成两个组 A B
# 从一个数组中增加一个元素进 A 就要从另一个数组从 A 减少一个元素
# 当保证第一组的最大值 <= 第二组的最小值

from math import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): # 交换保证长度短的在前,可以从 i = 0 枚举
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        if m == 0:
            return nums2[n // 2] if n % 2 else (nums2[n // 2] + nums2[n // 2 - 1]) / 2
        # nums1 有 i 个数在第一组 nums2 有 j = (m + n + 1) // 2 - i 个在第一组
        # 偶数的时候均分, 奇数
        i, j = 0, (m + n + 1) // 2 
        max1 = nums2[j - 1] # 第一组的最大值
        min2 = nums1[i] if j > n - 1 else min(nums1[i], nums2[j]) # 第二组最小值

        while True:
            if max1 <= min2: # 满足要求
                return max1 if (m + n) % 2 else (max1 + min2) / 2
            # 添加 nums1 的一个数进入一组，从nums2减少一个数进入一组
            i += 1
            j -= 1
            max1 = nums1[i - 1] if j == 0 else max(nums1[i - 1], nums2[j - 1])
            min2 = nums2[j] if i == m else min(nums1[i], nums2[j])

# 采用二分法搜索 i
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        def get_val(nums: List[int], idx:int) -> int:
            if 0 <= idx < len(nums):
                return nums[idx]
            else:
                return -inf if idx < 0 else inf

        left, right = 0, m
        while left <= right: # 元素存在
            # i: nums1 中第二组数开始的下标(第一组数的个数)
            # j: nums2 中第二组数开始的下标(第一组数的个数) j = ⌊(m + n + 1) / 2 ⌋ - i
            # i in [0, m] 且 m <= n -> j in [0, ⌊(m + n + 1) / 2 ⌋] (即在 [0, n] 中)
            # 最终目标找到一个 i 使得: max(nums1[i - 1], nums2[j - 1]) <= min(nums1[i], nums2[j])
            # 又因为 nums1[i - 1] < nums1[i] 且 nums2[j - 1] < nums2[j]
            # 故上述条件化简为:
            #   1. nums1[i - 1] <= nums2[j]
            #   2. nums1[i] >= nums2[j - 1]
            # 假设当 nums1, nums2 下标为 -1 时为 -inf 超出数组长度时为 inf
            
            # 循环不变式
            # left - 1 的 i 有 nums1[i] <= nums2[j] (nums1[i] > nums2[i - 1] => nums1[i - 1] < nums2[j])
            # right + 1 的 i 有 nums1[i] >= nums2[j] (nums2[j] > nums2[j - 1] => nums1[i] > nums2[j - 1])
            mid = (left + right) >> 1
            j = (m + n + 1) // 2 - mid
            val_1 = get_val(nums1, mid)
            val_2 = get_val(nums2, j)
            if val_1 <= val_2:
                left = mid + 1
            else:
                right = mid - 1
        i_idx = right
        j_idx = (m + n + 1) // 2 - i_idx
        max_group_1 = max(get_val(nums1, i_idx - 1), get_val(nums2, j_idx - 1))
        min_group_2 = min(get_val(nums1, i_idx), get_val(nums2, j_idx))
        return max_group_1 if (m + n) % 2 else (max_group_1 + min_group_2) / 2

    def test(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        res = self.findMedianSortedArrays(nums1, nums2)

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()