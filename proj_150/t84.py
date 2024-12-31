# 题目：102.二叉树的层序遍历
# 标签：树 BFS 二叉树
# 难度：中等
# 日期：12.23

from typing import *

# 思路:
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root:
            visit_que = deque([root])
            while visit_que:
                level_size = len(visit_que)
                vals = []
                for _ in range(level_size):
                    node = visit_que.popleft()
                    vals.append(node.val)
                    if node.left: visit_que.append(node.left)
                    if node.right: visit_que.append(node.right)
                ans.append(vals)
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