# 题目：129.求根节点到叶节点数字之和
# 标签：树 DFS 二叉树
# 难度：中等
# 日期：12.22

from typing import *
from collections import deque

# 思路:
# DFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        def dfs(node:Optional[TreeNode], val:int) -> None:
            if node:
                tmp = val * 10 + node.val
                if not node.left and not node.right: # leaf
                    nonlocal total_sum
                    total_sum += tmp
                if node.left:
                    dfs(node.left, tmp)
                if node.right:
                    dfs(node.right, tmp)
        dfs(root, 0)
        return total_sum

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
# dfs带返回值的写法
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], x:int=0) -> int:
        if root is None:
            return 0
        x = x * 10 + root.val
        if root.left is root.right: # left == right == None
            return x
        return self.sumNumbers(root.left, x) + self.sumNumbers(root.right, x)
# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()