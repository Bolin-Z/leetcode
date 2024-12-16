# 题目：3. 无重复字符的最长子串
# 标签：哈希 字符串 滑动窗口
# 难度：中等
# 日期：12.16

from typing import *

# 思路:
# 和 209.长度最小的子数组 相似
# 用一个哈希集合维护现有的字符，然后用滑动窗口移动左右指针

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        max_len, left = 0, 0
        for right, c in enumerate(s):
            while c in hash_set:
                hash_set.remove(s[left])
                left += 1
            hash_set.add(c)
            max_len = max(max_len, right - left + 1)
        return max_len
        

        
    def test(self):
        """test code
        """
        test_cases = [
            ["abcabcbb"],
            ["bbbbb"],
            ["pwwkew"]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.lengthOfLongestSubstring(case[0])
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