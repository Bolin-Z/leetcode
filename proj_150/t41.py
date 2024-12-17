# 题目：290.单词规律
# 标签：哈希 字符串
# 难度：简单
# 日期：12.17

from typing import *

# 思路:
# 和 t40 205.同构字符串 一样，变成单词而已

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        f, g = {}, {}
        for i, p in enumerate(pattern):
            word = words[i]
            if p in f and word in g:
                if f[p] != word or g[word] != p:
                    return False
            elif p not in f and word not in g:
                f[p], g[word] = word, p
            else:
                return False
        return True

    def test(self):
        """test code
        """
        test_cases = [
            ["abba", "dog cat cat dog"]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.wordPattern(case[0], case[1])
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