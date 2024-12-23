# 题目：399.除法求值
# 标签：DFS BFS 并查集 图 数组 字符串 最短路
# 难度：中等
# 日期：12.23

from typing import *

# 思路:
# A / B 表示存在 A 到 B 的有向链接
# C / D 即在图上找到一条从 C 到 D 的 path

from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        div_ans:Dict[str, Dict[str, float]] = dict()
        for idx, eq in enumerate(equations):
            var1, var2 = eq
            if var1 not in div_ans: div_ans[var1] = dict()
            if var2 not in div_ans: div_ans[var2] = dict()
            div_ans[var1][var2] = values[idx]
            div_ans[var2][var1] = 1 / values[idx]
        
        ans = []
        for idx, query in enumerate(queries):
            src, des = query
            if src in div_ans and des in div_ans:
                visit_que = deque([(src, 1.0)])
                visited = set([src])
                while visit_que:
                    cur, val = visit_que.popleft()
                    if des in div_ans[cur]:
                        ans.append(val * div_ans[cur][des])
                        break
                    else:
                        for key, value in div_ans[cur].items():
                            if key not in visited:
                                visited.add(key)
                                visit_que.append([key, val * value])
            if len(ans) < idx + 1: ans.append(-1.0)
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
# 并查集的思路

class UnionFindSet:
    def __init__(self, n:int) -> None:
        self.__parent = [-1 for _ in range(n)]
        self.__weight = [0.0 for _ in range(n)]
    def find(self, id:int) -> int:
        if self.__parent[id] != -1:
            origin = self.__parent[id]
            self.__parent[id] = self.find(self.__parent[id])
            self.__weight[id] *= self.__weight[origin]
        return self.__parent[id]
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        pass

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()