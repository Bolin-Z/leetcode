# 题目：13. 罗马数字转整数
# 标签：哈希表 数字 字符串
# 难度：简单

from typing import *

# 思路:
#

class Solution:
    def romanToInt(self, s: str) -> int:
        hash_table ={
            'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        ans = 0
        last_number = 0
        # for i in range(len(s) - 1, -1, -1):
        #     cur_number = hash_table[s[i]]
        #     if cur_number < last_number:
        #         ans -= cur_number
        #     else:
        #         ans += cur_number
        #     last_number = cur_number
        # 使用 reversed(s) 加速
        for c in reversed(s):
            cur_number = hash_table[c]
            if cur_number < last_number:
                ans -= cur_number
            else:
                ans += cur_number
            last_number = cur_number
        return ans

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