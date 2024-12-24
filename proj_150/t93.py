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

class DisjointSetWithWeight:
    def __init__(self):
        self._parents = []
        self._weights = []
        self._token_to_id:Dict[str, int] = {}
        self._id_to_token:Dict[int, str] = {}

    def add(self, token:str) -> None:
        if token not in self._token_to_id:
            new_id = len(self._token_to_id)
            self._token_to_id[token] = new_id
            self._id_to_token[new_id] = token
            self._parents.append(new_id)
            self._weights.append(1.0)
    
    def union(self, x:str, y:str, weight:float) -> None:
        self.add(x)
        self.add(y)
        self._union(self._token_to_id[x], self._token_to_id[y], weight)
    
    def query_weight(self, x:str, y:str) -> float:
        if x in self._token_to_id and y in self._token_to_id:
            rootx_id = self._find(self._token_to_id[x])
            rooty_id = self._find(self._token_to_id[y])
            if rootx_id == rooty_id:
                return self._weights[self._token_to_id[x]] / self._weights[self._token_to_id[y]]
        return -1.0
    
    def _find(self, id:int) -> int:
        if id != self._parents[id]: # 当前不为根节点
            origin = self._parents[id]
            self._parents[id] = self._find(self._parents[id]) # 递归寻根 + 路径压缩
            self._weights[id] *= self._weights[origin] # self._weights[origin] 的值在递归寻根时已经保证为到根节点的权重
        return self._parents[id]
    
    def _union(self, x:int, y:int, weight:float) -> None:
        rootx = self._find(x)
        rooty = self._find(y)
        if rootx != rooty: # 合并
            self._parents[rootx] = rooty # 将 rootx 连到 rooty
            self._weights[rootx] = self._weights[y] * weight / self._weights[x] # 更新 rootx 到 rooty 的权重
    
    def _cal_weight(self, x:int, y:int) -> float:
        rootx = self._find(x)
        rooty = self._find(y)
        return self._weights[x] / self._weights[y] if rootx == rooty else -1.0

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        disjoint_set =  DisjointSetWithWeight()
        for idx, eq in enumerate(equations):
            var1, var2 = eq
            weight = values[idx]
            disjoint_set.union(var1, var2, weight)
        ans = []
        for eq in queries:
            var1, var2 = eq
            ans.append(disjoint_set.query_weight(var1, var2))
        return ans

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()