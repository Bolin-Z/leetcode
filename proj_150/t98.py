# 题目：208.实现Trie(前缀树)
# 标签：设计 字典树 哈希表 字符串
# 难度：中等
# 日期：12.25

from typing import *

# 思路:
#
class TreeNode:
    def __init__(self, isword:bool=False) -> None:
        self.isword:bool = isword
        self.childs:Dict[str, TreeNode] = {}

class Trie:

    def __init__(self):
        self.root = TreeNode(False)

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.childs:
                ptr.childs[c] = TreeNode(isword=False)
            ptr = ptr.childs[c]
        ptr.isword = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            if c not in ptr.childs:
                return False
            ptr = ptr.childs[c]
        return ptr.isword

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if c not in ptr.childs:
                return False
            ptr = ptr.childs[c]
        return True

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