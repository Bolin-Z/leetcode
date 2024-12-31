# 题目：173.二叉搜索树迭代器
# 标签：栈 树 设计 二叉搜索树 迭代器
# 难度：中等
# 日期：12.22

from typing import *
from collections import deque

# 思路:
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.visit_stack = deque([root])
        ptr = root.left
        while ptr:
            self.visit_stack.append(ptr)
            ptr = ptr.left
        self.next_val = self.visit_stack[-1].val - 1

    def next(self) -> int:
        top = self.visit_stack.pop()
        ptr = top.right
        while ptr:
            self.visit_stack.append(ptr)
            ptr = ptr.left
        return top.val

    def hasNext(self) -> bool:
        return len(self.visit_stack) != 0

class Solution:
    def test(self):
        node = {n.val:n for n in [TreeNode(val=i) for i in [7, 3, 15, 9, 20]]}
        root = node[7]
        node[7].left = node[3]
        node[7].right = node[15]
        node[15].left = node[9]
        node[15].right = node[20]
        iter = BSTIterator(root)
        iter.next()
        iter.next()
        iter.hasNext()
        iter.next()
        iter.hasNext()
        iter.next()
        iter.hasNext()

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()