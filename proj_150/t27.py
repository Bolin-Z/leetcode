# 题目：167. 两数之和 II 输入有序数组
# 标签：数组 双指针 二分查找
# 难度：中等
# 日期：12.15

from typing import *

# 思路:
# 一个指针 i 从0开始，另一个在 [i, n) 之间寻找一个 数等于 target nums[i]

class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     first_idx = 0
    #     while target - (numbers[first_idx] * 2) >= 0:
    #         second_idx = self.binary_search(numbers, first_idx + 1, len(numbers), target - numbers[first_idx])
    #         if second_idx != -1:
    #             return [first_idx + 1, second_idx + 1]
    #         first_idx += 1
    #     # not found
    #     return [-1, -1]
    
    # def binary_search(self, numbers:List[int], left:int, right:int, val:int):
    #     """
    #     找到在 [left, right) 区间等于 val 的数
    #     """
    #     if left == right:
    #         # 不存在
    #         return -1
    #     mid = (left + right) >> 1
    #     guess_val = numbers[mid]
    #     if guess_val == val:
    #         return mid
    #     elif guess_val > val:
    #         return self.binary_search(numbers, left, mid, val)
    #     else:
    #         return self.binary_search(numbers, mid + 1, right, val)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 双指针法
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1


    def test(self):
        """test code
        """
        test_cases = []
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = []
            for ans in answer:
                print(f"\t\t{ans}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()