# 题目：100.相同的树
# 标签：
# 难度：简单
# 日期：12.20

from typing import *

# 思路:
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.__check_tree(p, q)
    
    def __check_tree(self, p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p and q:
            return p.val == q.val and self.__check_tree(p.left, q.left) and self.__check_tree(p.right, q.right)
        return False

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