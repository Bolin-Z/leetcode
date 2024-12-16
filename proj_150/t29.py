# 题目：15. 三数之和
# 标签：数组 双指针 排序
# 难度：中等
# 日期：12.15

from typing import *

# 思路:
# 与 t27 两数之和 II 输入有序数组类似?
# 先排序成非递减序列
# 固定一个指针，移动另外两个

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        first, second, third = 0, 0, 0
        last_first = None
        while first < len(nums) - 2 and nums[first] <= 0:
            if nums[first] != last_first:
                last_first = nums[first]
                second = first + 1
                third = len(nums) - 1
                last_second, last_third = None, None
                while second < third:
                    sum = last_first + nums[second] + nums[third]
                    if sum == 0:
                        if not (nums[second] == last_second and nums[third] == last_third):
                            # 找到新的
                            last_second, last_third = nums[second], nums[third]
                            answer.append([last_first, last_second, last_third])
                        second += 1
                        third -= 1
                    elif sum < 0:
                        second += 1
                    elif sum > 0:
                        third -= 1
            first += 1
        return answer

    def test(self):
        """test code
        """
        test_cases = [
            [-2,0,0,2,2],
            [-1,0,1,2,-1,-4],
            [0,1,1],
            [0,0,0]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.threeSum(case)
            for ans in answer:
                print(f"\t\t{ans}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()