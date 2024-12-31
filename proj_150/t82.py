# 题目：199.二叉树的右视图
# 标签：树 DFS BFS 二叉
# 难度：中等
# 日期：12.23

from typing import *

# 思路:
# 层序遍历

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root:
            cur_level:List[TreeNode] = [root]
            while cur_level:
                next_level = []
                ans.append(cur_level[-1].val)
                for n in cur_level:
                    if n.left: next_level.append(n.left)
                    if n.right: next_level.append(n.right)
                cur_level = next_level
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
# 递归版本 DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node: Optional[TreeNode], depth:int) -> None:
            if node is None: return
            if depth == len(ans): # 该深度首次遇到
                ans.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return ans

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()