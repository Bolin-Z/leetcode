# 题目：14.最长公共前缀
# 标签：字典树 字符串
# 难度：简单

from typing import *

# 思路:
#

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for str in strs:
            new_prefix = ""
            check_len = min(len(prefix), len(str))
            for i in range(check_len):
                if str[i] == prefix[i]:
                    new_prefix += str[i]
                else:
                    break
            prefix = new_prefix
            if prefix == "":
                break
        return prefix

    def test(self):
        """test code
        """
        test_cases = []
        pass

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()