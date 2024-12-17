# 题目：219.存在重复元素
# 标签：数组 哈希 滑窗
# 难度：简单
# 日期：12.17

from typing import *

# 思路:
# 可以用一个哈希表存
# 尝试使用滑动窗口, 维护一个大小为k的哈希表, 省空间

# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         table = {}
#         for i, n in enumerate(nums):
#             if n in table:
#                 if i - table[n] <= k:
#                     return True
#             table[n] = i
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = set()
        for i, n in enumerate(nums):
            if i > k:
                table.remove(nums[i - k - 1])
            if n in table:
                return True
            table.add(n)
        return False

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

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()