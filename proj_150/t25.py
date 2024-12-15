# 题目：125.验证回文串
# 标签：双指针 字符串
# 难度：简单
# 日期：12.15

from typing import *

# 思路:
#

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            left_code = self.transform(ord(s[left]))
            right_code = self.transform(ord(s[right]))
            if left_code != -1 and right_code != -1:
                if left_code != right_code:
                    return False
                else:
                    left += 1
                    right -= 1
            if left_code == - 1: left += 1
            if right_code == - 1: right -= 1
        return True

    def transform(self, x:int) -> int:
        if x >= 48 and x <= 57: # 数字
            return x
        if x >= 65 and x <= 90: # 大写字母
            return x
        if x >= 97 and x <= 122: # 小写字母
            return 65 + x - 97
        # 非字母数字字符
        return -1


    def test(self):
        """test code
        """
        test_cases = [
            "A man, a plan, a canal: Panama"
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.isPalindrome(case)
            for ans in answer:
                print(f"\t\t{ans}")

# 官方题解
# python特性
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         if s == ' ':
#             return True
#         s2 = s.lower()
#         s2 = ''.join(filter(str.isalnum, s2.encode('ascii')))
#         s3 = s2[::-1]
#         return s2 == s3

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()