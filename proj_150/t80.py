# 题目：222.完全二叉树的节点个数 *
# 标签：位运算 树 二分查找 二叉树
# 难度：简单
# 日期：12.22

from typing import *
from collections import deque

# 思路:
# 先一直向左遍历统计层数

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = deque([root])
        cnt = 0
        while stack:
            top = stack.popleft()
            cnt += 1
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return cnt

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
# 评论区Lzh：判断当前节点引导的子树是不是满二叉，
# 是的话可以直接返回节点数，不是就往下遍历
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l_depth, r_depth = 0, 0
        ptr = root
        while ptr.left:
            l_depth += 1
            ptr = ptr.left
        ptr = root
        while ptr.right:
            r_depth += 1
            ptr = ptr.right
        if l_depth == r_depth: # 满二叉
            return 2 ** (l_depth + 1) - 1
        else: # 非满二叉
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()