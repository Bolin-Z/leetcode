# 题目：42. 接雨水
# 标签：栈 数组 双指针 动态规划 单调栈
# 难度：困难

from typing import *

# 思路:
#

class Solution:
    def trap(self, height: List[int]) -> int:
        return self.mono_stack(height)
    
    def mono_stack(self, height:List[int]) -> int:
        # 使用一个单调非增的栈
        # 从栈底到栈顶，单调非增；栈顶到栈底，单调非减
        # 栈内存放下标
        ans = 0
        stack = list()
        n = len(height)
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                curWidth = i - left - 1
                curHeight = min(height[left], height[i]) - height[top]
                ans += curWidth * curHeight
            stack.append(i)
        return ans
    
    def dp(self, height:List[int]) -> int:
        # 每个位置 i 可以存储的水量为 i 左边最高的位置与 i 右边最高的位置 的最小值减去位置 i 的高度
        # left_max 数组存储
        n = len(height)
        left_max = [0 for _ in range(n)]
        right_max = [0 for _ in range(n)]
        
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        ans  = 0
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans

    def dp2(self, height:List[int]) -> int:
        # dp 优化
        # 使用双指针 left right 以及维护两个变量 left_max 和 right_max
        # 当 height[left] < height[right] 时有 left_max < right_max
        #   进一步对于该位置 i = left 来说 left_max[i] < right_max[i] 根据更新规则
        #   填充该位置水量 water = left_max - height[i]
        #   同时向右移动left指针
        # 反之 height[left] >= height[right] 时对于位置 i = right 来说 left_max[i] > right_max[i]
        #   填充该位置水量 water = right_max - height[right]
        #   同时向左移动right指针
        n = len(height)
        left, right = 0, n - 1
        left_max = right_max = 0
        ans = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans

    def test(self):
        """test code
        """
        test_cases = []
        pass

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()