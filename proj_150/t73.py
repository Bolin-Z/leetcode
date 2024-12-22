# 题目：105.从前序与中序遍历构造二叉树
# 标签：树 数组 哈希 分治 二叉
# 难度：中等
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
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if len(preorder) == 0: return None
    #     root = TreeNode()
    #     root.val = preorder[0]
    #     idx = inorder.index(root.val)
    #     root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
    #     root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
    #     return root
# 迭代法
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: # empty
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        inorder_idx = 0
        for i in range(1, len(preorder)):
            preorder_val = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorder_idx]: # 当前preorder中的值为栈顶值的左节点
                node.left = TreeNode(preorder_val)
                stack.append(node.left)
            else: # 当前的pretender的值为stack中某个节点的右节点
                while stack and stack[-1].val == inorder[inorder_idx]:
                    node = stack.pop()
                    inorder_idx += 1
                node.right = TreeNode(preorder_val)
                stack.append(node.right)
        return root

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