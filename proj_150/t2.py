# 27.移除元素
# 数组 双指针

# class Solution {
# public:
#     int removeElement(vector<int>& nums, int val) {
#         int n = nums.size();
#         int left = 0;
#         for (int right = 0; right < n; right++) {
#             if (nums[right] != val) {
#                 nums[left] = nums[right];
#                 left++;
#             }
#         }
#         return left;
#     }
# };

# class Solution {
# public:
#     int removeElement(vector<int>& nums, int val) {
#         int left = 0, right = nums.size();
#         while (left < right) {
#             if (nums[left] == val) {
#                 nums[left] = nums[right - 1];
#                 right--;
#             } else {
#                 left++;
#             }
#         }
#         return left;
#     }
# };

from typing import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        tail = len(nums)
        while count < tail:
            if nums[count] == val:
                tail -= 1
                # 因为不care值，甚至可以不交换
                # nums[tail], nums[count] = nums[count], nums[tail]
                nums[count] = nums[tail]
                count -= 1
            count += 1
        return count