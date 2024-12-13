# 题目：45.跳跃游戏II
# 标签：贪心 数组 动态规划
# 难度：中等

from typing import *

# 思路:
# 

class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_index = 0
        cur_reachable = 0
        next_reachable = 0
        last_index = len(nums) - 1
        jump_cnt = 0
        while cur_reachable < last_index:
            if cur_index + nums[cur_index] > next_reachable:
                next_reachable = cur_index + nums[cur_index]
            if cur_index == cur_reachable:
                cur_reachable = next_reachable
                jump_cnt += 1
            cur_index += 1
        return jump_cnt

    def test(self):
        """test code
        """
        test_cases = [
            [2,3,1,1,4],
            [2,3,0,1,4],
            [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3], # 2
            [0] # 0
        ]
        for i, case in enumerate(test_cases):
            print(f"用例: {i}\n\t输入: {case}\n\t输出: {self.jump(case)}")
        pass

# 官方题解
# 改成 for 循环
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if i <= maxPos:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()