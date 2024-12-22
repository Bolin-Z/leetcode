# 题目：106.从中序与后序遍历构造二叉树
# 标签：树 数组 哈希 分治 二叉
# 难度：中等
# 日期：12.21

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.__iteration(inorder, postorder)
    
    def __recursion(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def construct_tree(inorder:List[int], postorder:List[int]) -> Optional[TreeNode]:
            if postorder:
                root = TreeNode(postorder[-1])
                idx = inorder.index(root.val)
                root.left = construct_tree(inorder[:idx], postorder[:idx])
                root.right = construct_tree(inorder[idx + 1:], postorder[idx:len(postorder) - 1])
                return root
            return None
        return construct_tree(inorder, postorder)
    
    def __iteration(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        stack = [root]
        inorder_idx = len(inorder) - 1
        for i in range(len(postorder) - 2, -1, -1):
            postorder_val = postorder[i]
            node = stack[-1]
            if node.val != inorder[inorder_idx]:
                node.right = TreeNode(postorder_val)
                stack.append(node.right)
            else:
                while stack and stack[-1].val == inorder[inorder_idx]:
                    node = stack.pop()
                    inorder_idx -= 1
                node.left = TreeNode(postorder_val)
                stack.append(node.left)
        return root
    

    def test(self):
        """test code
        """
        test_cases = [
            {
                "Input ": [[9,3,15,20,7], [9,15,7,20,3]],
                "Expect": [],
                "Output": []
            }
        ]
        for i, case in enumerate(test_cases):
            case["Output"].append(self.buildTree(case["Input "][0], case["Input "][1])) # 调用求解
            print(f"Test {i + 1}")
            for key, val in case.items():
                print(f"\t\t{key}: {val}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()