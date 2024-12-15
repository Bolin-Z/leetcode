# 题目：392. 判断子序列
# 标签：双指针 动规 字符串 
# 难度：简单
# 日期：12.15

from typing import *

# 思路:
#

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        match_ptr = 0
        check_ptr = 0
        while match_ptr < len(s) and check_ptr < len(t):
            if s[match_ptr] == t[check_ptr]:
                match_ptr += 1
            check_ptr += 1 
        return match_ptr == len(s)

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
            for ans in answer:
                print(f"\t\t{ans}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()