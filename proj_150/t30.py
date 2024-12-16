# 题目：209.长度最小的子数组
# 标签：数组 二分 前缀和 滑窗
# 难度：中等
# 日期：12.15

from typing import *
from math import inf

# 思路:
# 维护两个指针

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = inf
        array_sum, array_len = 0, 0
        left = right = 0
        while right < len(nums):
            array_sum += nums[right]
            array_len += 1
            if array_sum >= target:
                min_len = min(array_len, min_len)
                while left < right:
                    array_sum -= nums[left]
                    array_len -= 1
                    left += 1
                    if array_sum >= target:
                        min_len = min(array_len, min_len)
                    else:
                        break
            right += 1
        if min_len == inf:
            return 0
        else:
            return min_len

    def test(self):
        """test code
        """
        test_cases = [
            [
                7, [2,3,1,2,4,3]
            ]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.minSubArrayLen(case[0], case[1])
            if type(answer) == List:
                for ans in answer:
                    print(f"\t\t{ans}")
            else:
                print(f"\t\t{answer}")

# 官方题解
# 简洁写法
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        s = left = 0
        for right, x in enumerate(nums):
            s += x
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right - left + 1)
        return ans if ans <= n else 0
# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()