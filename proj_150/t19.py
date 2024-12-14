# 题目：58.最后一个单词的长度
# 标签：字符串
# 难度：简单

from typing import *

# 思路:
#

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        ptr = n - 1
        while s[ptr] == ' ':
            ptr -= 1
        answer = 0
        while s[ptr] != ' ' and ptr > -1:
            answer += 1
            ptr -= 1
        return answer

    def test(self):
        """test code
        """
        test_cases = []
        pass

# 官方题解
# 人生苦短我用python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()