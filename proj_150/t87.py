# 题目：530.二叉搜索树的最小绝对差值
# 标签：树 DFS BFS 二叉搜索树 二叉树
# 难度：简单
# 日期：12.23

from typing import *

# 思路:
# 二叉搜索树中序遍历就是有序数组

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from math import inf
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff, last_val = inf, inf
        visit_stack = [root]
        while visit_stack[-1].left:
            visit_stack.append(visit_stack[-1].left)
        while visit_stack:
            node = visit_stack.pop()
            min_diff = min(min_diff, abs(node.val - last_val))
            last_val = node.val
            if node.right:
                visit_stack.append(node.right)
                while visit_stack[-1].left:
                    visit_stack.append(visit_stack[-1].left)
        return min_diff

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
# 使用递归实现
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pre, ans = -1, inf
        def dfs(node: TreeNode) -> None:
            if node is None: return
            nonlocal pre, ans
            dfs(node.left)
            x = node.val
            if pre != -1: ans = min(ans, x - pre)
            pre = x
            dfs(node.right)
        dfs(root)
        return ans
# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()