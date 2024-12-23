# 题目：114.二叉树展开为链表
# 标签：栈 树 DFS 链表 二叉树
# 难度：中等
# 日期：12.22

from typing import *

# 思路:
# 先序遍历的方式递归访问构造链表，返回链表的尾部

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            self.tree_2_list(root)

    def tree_2_list(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        left, right, tail = root.left, root.right, root
        if left:
            tail = self.tree_2_list(left)
            root.left = None
            root.right = left
        if right:
            new_tail = self.tree_2_list(right)
            tail.left = None
            tail.right = right
            tail = new_tail
        return tail


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
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)
        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        return right_tail or left_tail or root


# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()