# 题目：151. 反转字符串中的单词
# 标签：双指针 字符串
# 难度：中等

from typing import *

# 思路:
#

class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.strip().split()
        words_list.reverse()
        answer = " ".join(words_list)
        return answer.strip()

    def test(self):
        """test code
        """
        test_cases = []
        pass

# 官方题解
# 人生苦短
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()