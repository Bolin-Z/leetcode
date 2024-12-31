# 题目：210.课程表II
# 标签：DFS BFS 图 拓扑排序
# 难度：中等
# 日期：12.24

from typing import *
from collections import deque

# 思路:
# 与 t94 207.课程表 一样的思路

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        neighbors = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for prerequest in prerequisites:
            c1, c2 = prerequest
            neighbors[c2].append(c1)
            indegree[c1] += 1
        que = deque()
        for idx in range(numCourses):
            if indegree[idx] == 0:
                que.append(idx)
        ans = []
        while que:
            idx = que.popleft()
            ans.append(idx)
            for n in neighbors[idx]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    que.append(n)       
        return ans if len(ans) == numCourses else []

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