# 题目：242.有效的字母异位词
# 标签：哈希 字符串 排序
# 难度：简单
# 日期：12.17

from typing import *

# 思路:
# 用两个哈希表，分别统计 s t 中每个字符出现次数，出现次数不一致就不可以
# 化简为一个可以

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for c in s:
            if c not in counter: counter[c] = 0
            counter[c] += 1
        for c in t:
            if c not in counter: return False
            elif counter[c] < 1: return False
            counter[c] -= 1
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
# 人生苦短我用python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()