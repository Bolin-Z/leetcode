# 题目：211.添加与搜索单词-数据结构设计
# 标签：DFS 字典树 字符串
# 难度：中等
# 日期：12.25

from typing import *
from collections import *
from math import *

# 思路:
# 字典树 + DFS

class TreeNode:
    def __init__(self, isword:bool=False) -> None:
        self.isword = isword
        self.childs:Dict[str,TreeNode] = {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode(False)

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.childs:
                ptr.childs[c] = TreeNode(False)
            ptr = ptr.childs[c]
        ptr.isword = True

    def search(self, word: str) -> bool:
        return self._search(self.root, word)

    def _search(self, node:TreeNode, word:str) -> bool:
        ptr = node
        for idx,c in enumerate(word):
            if c == ".":
                for val in ptr.childs.values():
                    if self._search(val, word[idx+1:]):
                        return True
            if c not in ptr.childs:
                return False
            ptr = ptr.childs[c]
        return ptr.isword

class Solution:
    def test(self):
        """test code
        """
        test_cases = [
            {
                "Input ": [],
                "Expect": [],
                "Output": []
            }
        ]
        for i, case in enumerate(test_cases):
            case["Output"].append(case["Input "]) # 调用求解
            print(f"Test {i + 1}")
            for key, val in case.items():
                print(f"\t\t{key}: {val}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()