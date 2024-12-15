# 题目：28. 找出字符串中第一个匹配项的下标
# 标签：双指针 字符串 字符串匹配
# 难度：简单
# KMP算法

from typing import *

# 思路:
#

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        next = self.build_next(needle)
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]: # 字符匹配 移动两个指针
                i += 1
                j += 1
            else:
                if j > 0: 
                    # needle 第 j 个字符不匹配 [0, j - 1] 匹配
                    # 通过next表回调 j
                    # next[j - 1] 为长度为 j 的子串的前后缀最大匹配长度
                    j = next[j - 1]
                else: # needle 第 0 个字符不匹配
                    i += 1
            if j == len(needle): # 匹配成功
                return i - j
        return -1 # 匹配失败
    
    def build_next(self, pattern) -> List[int]:
        next = [0]
        prefix_len = 0
        i = 1
        while i < len(pattern):
            if pattern[prefix_len] == pattern[i]:
                prefix_len += 1
                next.append(prefix_len)
                i += 1
            else: # 回退prefix_len
                if prefix_len == 0:
                    next.append(0)
                    i += 1
                else:
                    prefix_len = next[prefix_len - 1]
        return next

    def test(self):
        """test code
        """
        test_cases = [
            ["leetcode", "leeto"]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.strStr(case[0], case[1])
            for ans in answer:
                print(f"\t\t{ans}")

# 官方题解
# next数组的含义
# PMT的含义最大前后缀重叠长度

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()