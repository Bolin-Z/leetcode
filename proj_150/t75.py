# 题目：117.填充每个节点的下一个右侧节点指针II
# 标签：树 BFS DFS 链表 二叉树
# 难度：中等
# 日期：12.21

from typing import *
from collections import deque

# 思路:
# ！！！题目理解有出入，不是连到同层下一个右子节点，其实就是连到同层下一个节点
# 逐层遍历
# 遍历每一层的时候给下一层链接好
# 这样每一层的每个节点可以依赖与自己next的信息去给自己子层链接

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is not None:
            queue:Deque[Node] = deque()
            queue.append(root)
            while queue:
                node = queue.popleft()
                find = node.next
                while find:
                    if find.left:
                        find = find.left
                        break
                    elif find.right:
                        find = find.right
                        break
                    find = find.next
                if node.left:
                    node.left.next = node.right if node.right else find
                    queue.append(node.left)
                if node.right:
                    node.right.next = find
                    queue.append(node.right)
        return root

    def test(self):
        """test code
        """
        node = {n.val:n for n in [Node(val=i) for i in [1,2,3,4,5,7]]}
        root = node[1]
        root.left = node[2]
        root.right = node[3]
        node[2].left = node[4]
        node[2].right = node[5]
        node[3].right = node[7]
        self.connect(root)

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()