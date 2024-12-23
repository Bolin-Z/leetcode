# 题目：236.二叉树的最近公共祖先
# 标签：树 DFS 二叉
# 难度：中等
# 日期：12.23

from typing import *
from collections import deque

# 思路:
# 从根节点到对应节点上重合的最后一个节点

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(root:TreeNode, n:TreeNode) -> Deque[TreeNode]:
            if root is None: None
            if root is n:
                return deque([n])
            if root.left:
                path = find_path(root.left, n)
                if path:
                    path.appendleft(root) 
                    return path
            if root.right:
                path = find_path(root.right, n)
                if path:
                    path.appendleft(root) 
                    return path
            return None

        path_p = find_path(root, p)
        path_q = find_path(root, q)
        for i in range(1, min(len(path_p), len(path_q))):
            if path_p[i] != path_q[i]:
                return path_p[i - 1]
        return p if len(path_p) < len(path_q) else q

    def test(self):
        node = {n.val:n for n in [TreeNode(i) for i in [3,5,1,6,2,0,8,7,4]]}
        left = [
            (3,5), (5,6), (1,0), (2,7)
        ]
        right = [
            (3,1), (5,2), (1,8), (2,4)
        ]
        for i,j in left:
            node[i].left = node[j]
        for i,j in right:
            node[i].right = node[j]
        self.lowestCommonAncestor(node[3], node[5], node[4])


# 官方题解
# 另一种递归思路
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): 
            # 当为空或 p(q)时直接返回
            # 若 q(p) 在下面则 p(q) 一定是最近公共节点
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            # 如果左右子树都找到，说明当前节点为最近
            return root
        # 只有一边子树找到 那个子树有两个，则公共节点已经找到
        # 如果只有一个，那么公共节点也不为当前节点，为更高层的
        return left or right

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()