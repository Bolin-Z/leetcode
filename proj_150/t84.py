# 题目：637.二叉树的层平均值
# 标签：树 BFS DFS 二叉
# 难度：简单
# 日期：12.23

from typing import *
from statistics import mean

# 思路:
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        if root:
            cur_level:List[TreeNode] = [root]
            while cur_level:
                val = []
                next_level = []
                for n in cur_level:
                    val.append(n.val)
                    if n.left: next_level.append(n.left)
                    if n.right: next_level.append(n.right)
                ans.append(mean(val))
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

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()