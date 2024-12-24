# 题目：207.课程表
# 标签：BFS DFS 图 拓扑排序
# 难度：中等
# 日期：12.24

from typing import *
from collections import deque

# 思路:
# 有向图判环 使用拓扑排序 如果有节点无法排序就是有环

class Node:
    def __init__(self):
        self.outedges = []
        self.indegree = 0

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = [Node() for _ in range(numCourses)]
        for request in prerequisites:
            v1, v2 = request
            nodes[v1].outedges.append(v2)
            nodes[v2].indegree += 1
        que = deque()
        for node in nodes:
            if node.indegree == 0:
                que.append(node)
        while que:
            node = que.popleft()
            for n in node.outedges:
                nodes[n].indegree -= 1
                if nodes[n].indegree == 0:
                    que.append(nodes[n])
            numCourses -= 1
        return numCourses == 0

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