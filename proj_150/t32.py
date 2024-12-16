# 题目：30.串联所有单词的子串
# 标签：哈希 字符串 滑窗
# 难度：困难
# 日期：12.16

from typing import *

# 思路:
# 允许重复的 word
# 每个 word 视为一个 patt，用一个hashMap处理words {pattern:count}
# 对于 s 使用滑窗，每次移动一个 patt 的长度
# 同时维护一个 hashMap 当 match in hashMap 且个数小于时才加入否则一直 pop
# 补充考虑：需要开启多个滑窗！！因为可能从第 0,1,2,3,..., patt_len - 1 开始滑窗

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answer = []
        words_num, patt_len = len(words), len(words[0])
        patt_map = {}
        for word in words:
            if word in patt_map: patt_map[word] += 1
            else: patt_map[word] = 1
        for window_start in range(patt_len):
            left = right = window_start
            match = {}
            match_len = 0
            while right + patt_len - 1 < len(s):
                new_word = s[right:right + patt_len]
                if new_word in patt_map:
                    if new_word not in match: match[new_word] = 0
                    while not match[new_word] < patt_map[new_word]:
                        old_word = s[left:left + patt_len]
                        match[old_word] -= 1
                        left += patt_len
                        match_len -= 1
                    match[new_word] += 1
                    match_len += 1
                    if match_len == words_num:
                        answer.append(left)
                        old_word = s[left:left + patt_len]
                        match[old_word] -= 1
                        match_len -= 1
                        left += patt_len
                else:
                    match.clear()
                    left, match_len = right + patt_len, 0
                right += patt_len   
        return answer

    def test(self):
        """test code
        """
        test_cases = [
            ["cbarfoocthefoobarman", ["foo","bar"]]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.findSubstring(case[0], case[1])
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