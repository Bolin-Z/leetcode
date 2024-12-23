# 题目：230.二叉搜索树中第K小的元素
# 标签：树 DFS 二叉搜索树 二叉树
# 难度：中等
# 日期：12.23

from typing import *

# 思路:
# 中序遍历 累计

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter, ans = 0, None
        def dfs(node: TreeNode) -> None:
            nonlocal counter, ans
            if node is None or ans is not None:
                return
            dfs(node.left)
            counter += 1
            if counter == k:
                ans = node.val
                return
            dfs(node.right)
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
# 中序遍历迭代写法
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root: # 一路向左
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()