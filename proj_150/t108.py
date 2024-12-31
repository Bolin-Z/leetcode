# 题目：108.将有序数组转换为二叉搜索树(平衡的)
# 标签：树 二叉搜索树 数组 分治 二叉树
# 难度：简单
# 日期：12.26

from typing import *

# 思路:
# 数组有序, 抽中点

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bulid_tree(left:int, right:int) -> Optional[TreeNode]:
            if right < left:
                return None
            if left == right:
                return TreeNode(nums[left])
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = bulid_tree(left, mid - 1)
            root.right = bulid_tree(mid + 1, right)
            return root
        return bulid_tree(0, len(nums) - 1)

    def test(self):
        nums = [-10,-3,0,5,9]
        self.sortedArrayToBST(nums)

# 官方题解
# 简洁写法
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        m = len(nums) // 2
        return TreeNode(nums[m], self.sortedArrayToBST(nums[0:m]), self.sortedArrayToBST(nums[m+1:]))

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()