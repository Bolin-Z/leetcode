# 题目：68. 文本左右对齐
# 标签：数组 字符串 模拟
# 难度：困难

from typing import *
from collections import deque

# 思路:
#

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur_words_len = 0
        cur_words = deque()
        answer = []
        for word in words:
            n = len(word)
            if cur_words_len + n + len(cur_words) > maxWidth: # 假设将这个单词放入
                new_line = []
                space_length = maxWidth - cur_words_len
                if len(cur_words) == 1:
                    w = cur_words.popleft()
                    new_line.append(w)
                    new_line.append(" " * space_length)
                else:
                    space_num = space_length // (len(cur_words) -1)
                    addition = space_length % (len(cur_words) - 1)
                    w = cur_words.popleft()
                    new_line.append(w)
                    while cur_words:
                        new_line.append(" " * space_num)
                        if addition > 0:
                            new_line.append(" ")
                            addition -= 1
                        w = cur_words.popleft()
                        new_line.append(w)
                cur_words_len = 0
                answer.append("".join(new_line))
            cur_words_len += n
            cur_words.append(word)
        # 最后一行
        addition_space = maxWidth - cur_words_len - (len(cur_words) - 1)
        new_line = []
        w = cur_words.popleft()
        new_line.append(w)
        while cur_words:
            new_line.append(" ")
            w = cur_words.popleft()
            new_line.append(w)
        new_line.append(" " * addition_space)
        answer.append("".join(new_line))
        return answer

    def test(self):
        """test code
        """
        test_cases = [
            [
                ["This", "is", "an", "example", "of", "text", "justification."], 16
            ],
            [
                ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20
            ]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.fullJustify(case[0], case[1])
            print(f"\t\t{answer}")
            # for ans in answer:
            #     print(f"\t\t{ans}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()