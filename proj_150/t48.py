# 题目：228.汇总区间
# 标签：数组
# 难度：简单
# 日期：12.17

from typing import *

# 思路:
# 双指针

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        answer = []
        left, right = 0, 1
        while right < len(nums):
            if nums[right] != nums[right - 1] + 1:
                if left == right - 1:
                    answer.append(f"{nums[left]}")
                else:
                    answer.append(f"{nums[left]}->{nums[right - 1]}")
                left = right
            right += 1
        if left == right - 1:
            answer.append(f"{nums[left]}")
        else:
            answer.append(f"{nums[left]}->{nums[right - 1]}")
        return answer

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
            if type(answer) == List:
                for ans in answer:
                    print(f"\t\t{ans}")
            else:
                print(f"\t\t{answer}")

# 官方题解
# 分组循环，不需要写特判
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        i, n = 0, len(nums)
        while i < n:
            start = i
            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            s = str(nums[start])
            if start < i:
                s += "->" + str(nums[i])
            answer.append(s)
            i += 1
        return answer

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()