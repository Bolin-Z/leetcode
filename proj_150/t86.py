# 题目：103.二叉树的锯齿形层序遍历
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root:
            left_to_right = True
            visit_que = deque([root])
            while visit_que:
                vals = []
                level_size = len(visit_que)
                for _ in range(level_size):
                    node = visit_que.popleft()
                    vals.append(node.val)
                    if node.left: visit_que.append(node.left)
                    if node.right: visit_que.append(node.right)
                if left_to_right:
                    left_to_right = False
                    ans.append(vals)
                else:
                    left_to_right = True
                    ans.append(vals[::-1])
        return ans

    def test(self):
        node = {n.val:n for n in [TreeNode(val=i) for i in [3,9,20,15,7]]}
        node[3].left = node[9]
        node[3].right = node[20]
        node[20].left = node[15]
        node[20].right = node[7]
        self.zigzagLevelOrder(node[3])

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()