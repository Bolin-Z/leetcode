# 题目：128.最长连续序列
# 标签：并查集 数组 哈希
# 难度：中等
# 日期：12.17

from typing import *

# 思路:
# 简单方法，先排序再滑动窗口 O(nlogn)
# 用一个哈希集合放所有数，然后每次迭代
# 对于数 x 来说，如果 x - 1 存在就说明肯定已经迭代过了 就可以跳过


class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if len(nums) == 0: return 0
    #     nums.sort()
    #     ptr, cur_len, max_len = 1, 1, 1
    #     while ptr < len(nums):
    #         if nums[ptr] == nums[ptr - 1] + 1:
    #             cur_len += 1
    #         elif nums[ptr] != nums[ptr - 1]:
    #             max_len = max(cur_len, max_len)
    #             cur_len = 1
    #         ptr += 1
    #     max_len = max(cur_len, max_len)
    #     return max_len

    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        # for n in nums:
        for n in hash_set: # 对set迭代？是因为去重了吗
            if n - 1 not in hash_set:
                ptr = n + 1
                cur_len = 1
                while ptr in hash_set:
                    cur_len += 1
                    ptr += 1
                longest = max(longest, cur_len)
        return longest

    def test(self):
        """test code
        """
        test_cases = [
            [[1,2,0,1]],
            [[0,3,7,2,5,8,4,6,0,1]]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.longestConsecutive(case[0])
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