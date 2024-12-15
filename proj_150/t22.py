# 题目：6. Z字形变换
# 标签：字符串
# 难度：中等

from typing import *

# 思路:
#

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        answer = ""
        group_num = (numRows - 1) * 2
        n = len(s)
        for row in range(numRows):
            if row == 0 or row == numRows - 1:
                nxt_group = 0
                while nxt_group < n:
                    idx = nxt_group + row
                    if not idx < n:
                        break
                    answer += s[idx]
                    nxt_group += group_num
            else:
                nxt_group = 0
                while nxt_group < n:
                    idx = nxt_group + row
                    if not idx < n:
                        break
                    answer += s[idx]
                    idx = nxt_group + group_num - row
                    if not idx < n:
                        break
                    answer += s[idx]
                    nxt_group += group_num
            if len(answer) == n:
                break
        return answer

    def test(self):
        """test code
        """
        test_cases = [
            ["A", 1],
            ["PAYPALISHIRING", 3]
        ]
        for i, n in enumerate(test_cases):
            print(f"测试用例{i + 1}:")
            print(f"\t输入: {n[0]}")
            print(f"\t      {n[1]}")
            print(f"\t输出: {self.convert(n[0], n[1])}")
        

# 官方题解
# 更简洁的代码
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: # 转向
                flag = - flag
            i += flag
        return "".join(res)

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()