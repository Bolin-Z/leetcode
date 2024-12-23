# 题目：124.二叉树中的最大路径和 *
# 标签：树 DFS DP 二叉树
# 难度：困难
# 日期：12.22

from typing import *
from math import inf, sum

# 思路:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(n:Optional[TreeNode]) -> int:
            """
            计算从叶子节点到当前节点n的最大路径
            """
            if n is None:
                return 0
            left_sum = dfs(n.left)
            right_sum = dfs(n.right)
            nonlocal ans
            ans = max(ans, left_sum + right_sum + n.val)
            return max(max(left_sum, right_sum) + n.val, 0)
        dfs(root)
        return ans


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