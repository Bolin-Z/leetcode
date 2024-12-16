# 题目：76.最小覆盖子串
# 标签：哈希 字符串 滑动窗口
# 难度：困难
# 日期：12.16

from typing import *
from math import inf
from collections import deque

# 思路:
# 和 t32 30.串联所有单词的子串一样，秒了，更简单只用维护一个集合

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        patt_map = {}
        for c in t:
            if c not in patt_map: patt_map[c] = 0
            patt_map[c] += 1
        match = {}
        match_idx = deque()
        match_len, patt_len = 0, len(t)
        min_idx, min_len, ptr = -1, inf, 0
        while ptr < len(s):
            new_c = s[ptr]
            if new_c in patt_map:
                match_idx.append(ptr)
                if new_c not in match: match[new_c] = 0
                if match[new_c] < patt_map[new_c]: match_len += 1
                match[new_c] += 1
                while match_len == patt_len:
                    left_most = match_idx[0]
                    old_c = s[left_most]
                    match[old_c] -= 1
                    if match[old_c] < patt_map[old_c]:
                        match_len -= 1
                        right_most = match_idx[-1]
                        sub_len = right_most - left_most + 1
                        if sub_len < min_len:
                            min_idx, min_len = left_most, sub_len
                    match_idx.popleft()
            ptr += 1
        if min_idx < 0: return ""
        else: return s[min_idx:min_idx + min_len]

    def test(self):
        """test code
        """
        test_cases = [
            ["ADOBECODEBANC", "ABC"]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.minWindow(case[0], case[1])
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