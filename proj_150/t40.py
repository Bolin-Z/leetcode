# 题目：205.同构字符串
# 标签：哈希 字符串
# 难度：简单
# 日期：12.17

from typing import *

# 思路:
# 维护两个哈希表

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        n = len(s)
        f, g = {}, {}
        for i in range(n):
            c1, c2 = s[i], t[i]
            if c1 in f and c2 in g:
                if f[c1] != c2 or g[c2] != c1:
                    return False
            elif c1 not in f and c2 not in g:
                f[c1], g[c2] = c2, c1
            else:
                return False
        return True

    def test(self):
        """test code
        """
        test_cases = [
            ["foo", "bar"]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.isIsomorphic(case[0], case[1])
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