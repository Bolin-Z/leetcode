# 题目：427.建立四叉树
# 标签：树 数组 分治 矩阵
# 难度：中等
# 日期：12.27

from typing import *

# 思路:
#

# Definition for a QuadTree node.
class Node:
    def __init__(self, 
    val:bool=False, isLeaf:bool=False, 
    topLeft:Optional['Node']=None, topRight:Optional['Node']=None, 
    bottomLeft:Optional['Node']=None, bottomRight:Optional['Node']=None
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if len(grid) == 0:
            return None
        def helper(lr:int, lc:int, rr:int, rc:int) -> Optional['Node']:
            if lr == rr and lc == rc:
                return Node(val=(grid[lr][lc] == 1), isLeaf=True)
            midr = (lr + rr + 1) // 2
            midc = (lc + rc + 1) // 2
            tl = helper(lr, lc, midr - 1, midc - 1)
            tr = helper(lr, midc, midr - 1, rc)
            bl = helper(midr, lc, rr, midc - 1)
            br = helper(midr, midc, rr, rc)
            root = Node()
            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf \
                and (tl.val == tr.val == bl.val == br.val):
                root.isLeaf = True
                root.val = tl.val
            else:
                root.topLeft = tl
                root.topRight = tr
                root.bottomLeft = bl
                root.bottomRight = br
            return root
        return helper(0, 0, len(grid) - 1, len(grid) - 1)

    def test(self):
        grid = [
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0]
        ]
        self.construct(grid)

# 官方题解
# 递归 + 二维前缀和
# 如果全是1前缀和为当前面积
# 如果全是0前缀和为0

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()