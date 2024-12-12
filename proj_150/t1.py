# 88.合并两个有序数组

# 官方题解
# 使用了双指针，更加简洁

# def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     p1, p2 = m - 1, n - 1
#     tail = m + n - 1
#     while p1 >= 0 or p2 >= 0:
#         if p1 == -1:
#             nums1[tail] = nums2[p2]
#             p2 -= 1
#         elif p2 == -1:
#             nums1[tail] = nums1[p1]
#             p1 -= 1
#         elif nums1[p1] > nums2[p2]:
#             nums1[tail] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[tail] = nums2[p2]
#             p2 -= 1
#         tail -= 1

from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # boundary case
        # 多余了其实，else里面已经覆盖
        if m == 0:
            for cur_idx in range(n):
                nums1[cur_idx] = nums2[cur_idx]
        elif n == 0:
            pass
        else:
            # m > 0 && n > 0
            next_place_to_insert = m + n - 1
            next_num1_idx = m - 1
            next_num2_idx = n - 1
            while not next_place_to_insert < 0:
                # boundary case
                if next_num1_idx < 0:
                    while not next_num2_idx < 0:
                        nums1[next_place_to_insert] = nums2[next_num2_idx]
                        next_place_to_insert -= 1
                        next_num2_idx -= 1
                    break
                elif next_num2_idx < 0:
                    while not next_num1_idx < 0:
                        nums1[next_place_to_insert] = nums1[next_num1_idx]
                        next_place_to_insert -= 1
                        next_num1_idx -= 1
                    break
                else:
                    # next_num1_idx >= 0 and next_num2_idx >= 0
                    next_num_to_insert = 0
                    if nums1[next_num1_idx] > nums2[next_num2_idx]:
                        # insert nums from 1 to the tail
                        next_num_to_insert = nums1[next_num1_idx]
                        next_num1_idx -= 1
                    else:
                        next_num_to_insert = nums2[next_num2_idx]
                        next_num2_idx -= 1
                    nums1[next_place_to_insert] = next_num_to_insert
                    next_place_to_insert -= 1
