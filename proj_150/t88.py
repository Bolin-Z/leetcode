# 题目：98.验证二叉搜索树
# 标签：树 DFS 二叉搜索树 二叉树
# 难度：中等
# 日期：12.23

from typing import *

# 思路:
# 中序遍历 检查后一个是否大于前一个

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from math import inf
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, last = [], -inf
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.val > last:
                return False
            last = root.val
            root = root.right
        return True

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
# 递归方法实现
# 本质上是前序遍历
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 检查以root为根节点的树的所有节点是否在开区间 (lower, upper) 内
        def check(node:Optional[TreeNode], lower, upper) -> bool:
            if node is None: return True
            if node.val <= lower or upper <= node.val:
                return False
            check_left = check(node.left, lower, node.val)
            check_right = check(node.right, node.val, upper)
            return check_left and check_right
        return check(root, -inf, inf)

# 灵山
# 后序遍历 维护左右子树的最小最大值 再与当前节点比较 自底向上
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node:Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return inf, -inf
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            x = node.val
            if x <= l_max or x >= r_min:
                return -inf, inf # 上一层的永远会返回这个
            return min(l_min, x), max(r_max, x)
        return dfs(root)[1] != inf
# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()