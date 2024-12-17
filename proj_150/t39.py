# 题目：383.赎金信
# 标签：哈希 字符串 计数
# 难度：简单
# 日期：12.17

from typing import *

# 思路:
#

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in magazine:
            if c not in counter: counter[c] = 0
            counter[c] += 1
        for c in ransomNote:
            if c in counter:
                counter[c] -= 1
                if counter[c] < 0:
                    return False
            else: return False
        return True

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