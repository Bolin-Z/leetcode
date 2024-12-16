# 题目：11. 盛最多水的容器
# 标签：贪心 数组 双指针
# 难度：中等
# 日期：12.15

from typing import *

# 思路:
#

class Solution:
    def maxArea(self, height: List[int]) -> int:
        current_max = -1
        left, right = 0, len(height) - 1
        while left < right:
            square = (right - left) * min(height[left], height[right])
            if square > current_max:
                current_max = square
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return current_max

    def test(self):
        """test code
        """
        test_cases = [
            [1,8,6,2,5,4,8,3,7]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.maxArea(case)
            print(f"\t{answer}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()