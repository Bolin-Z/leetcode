# 题目：55.跳跃游戏
# 标签：贪心 数组 动态规划
# 难度：中等

from typing import *

# 思路:
# 直接遍历，记录当前可跳的最大距离是否大于最后一个坐标

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_index = 0
        reach_index = 0
        last_index = len(nums) - 1
        while cur_index <= reach_index:
            if reach_index >= last_index:
                break
            if cur_index +  nums[cur_index] > reach_index:
                reach_index = cur_index + nums[cur_index]
            cur_index += 1
        return reach_index >= last_index

    def test(self):
        """test code
        DO NOT SUBMIT!
        """
        test_cases = [
            [2,3,1,1,4]
        ]
        for i, case in enumerate(test_cases):
            self.canJump(case)

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()