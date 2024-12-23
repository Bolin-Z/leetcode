# 题目：112.路径总和
# 标签：树 二叉树 BFS DFS
# 难度：简单
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasPathSum_BFS(root, targetSum)

    def hasPathSum_BFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        que_node = deque([root])
        que_val = deque([root.val])
        while que_node:
            cur_node = que_node.popleft()
            cur_sum = que_val.popleft()
            if not cur_node.left and not cur_node.right:
                if cur_sum == targetSum:
                    return True
                continue
            if cur_node.left:
                que_node.append(cur_node.left)
                que_val.append(cur_sum + cur_node.left.val)
            if cur_node.right:
                que_node.append(cur_node.right)
                que_val.append(cur_sum + cur_node.right.val)
        return False

    def hasPathSum_DFS(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        targetSum -= root.val
        if not root.left and not root.righ:
            return targetSum == 0
        return self.hasPathSum_DFS(root.left, targetSum) or self.hasPathSum_DFS(root.right, targetSum)

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