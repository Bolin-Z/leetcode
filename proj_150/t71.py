# 题目：101.对称二叉树
# 标签：树 DFS BFS 二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.__iteration(root)

    def __recursion(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        return self.__check(root.left, root.right)

    def __check(self, p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        if p is not None and q is not None:
            return p.val == q.val and self.__check(p.left, q.right) and self.__check(p.right, q.left)
        return False

    def __iteration(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        check_stack = [[root.left, root.right]]
        while check_stack:
            p, q = check_stack.pop()
            if (p is None and q is not None) or (p is not None and q is None):
                return False
            elif p and q:
                if p.val != q.val: return False
                else:
                    check_stack.extend([[p.left, q.right],  [p.right, q.left]])
        return True

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