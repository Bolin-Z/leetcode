# 题目：67.二进制求和
# 标签：位运算 数学 字符串 模拟
# 难度：简单
# 日期：1.2

from typing import *

# 思路:
#

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        table = {
            # a, b, res : dig res
            ("0", "0", "0") : ("0", "0"),
            ("0", "0", "1") : ("1", "0"),
            ("0", "1", "0") : ("1", "0"),
            ("1", "0", "0") : ("1", "0"),
            ("1", "1", "0") : ("0", "1"),
            ("0", "1", "1") : ("0", "1"),
            ("1", "0", "1") : ("0", "1"),
            ("1", "1", "1") : ("1", "1")
        }
        ans = []
        res = "0"
        if len(a) < len(b):
            a, b = b, a
        m, n = len(a), len(b)
        for digit in range(m):
            da = a[m - 1 - digit]
            db = "0" if digit >= n else b[n - 1 - digit]
            dr, res = table[(da, db, res)]
            ans.append(dr)
        if res == "1":
            ans.append(res)
        return "".join(ans[::-1])


    def test(self):
        a = "1010"
        b = "1011"
        ans = self.addBinary(a, b)

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()