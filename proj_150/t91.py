# 题目：133.克隆图
# 标签：BFS DFS 图 哈希
# 难度：中等
# 日期：12.23

from typing import *

# 思路:
# 用哈希表存储对应节点的映射 + BFS维护一个构造节点列表

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors:List['Node'] = neighbors if neighbors is not None else []

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        new_clone = Node(node.val)
        origin_to_clone = {node:new_clone}
        visit_que:Deque[List[Node]] = deque([[node, new_clone]])
        while visit_que:
            orign, clone = visit_que.popleft()
            for n in orign.neighbors:
                if n not in origin_to_clone:
                    new_node = Node(n.val)
                    origin_to_clone[n] = new_node
                    visit_que.append([n, new_node])
                clone.neighbors.append(origin_to_clone[n])
        return new_clone

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