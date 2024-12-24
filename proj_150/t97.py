# 题目：433.最小基因变化
# 标签：BFS 哈希 字符串
# 难度：中等
# 日期：12.24

from typing import *
from collections import deque

# 思路:
# 对bank库建图 只相差一个字符的基因间存在一条无向边
# 将 start 加入，连边，最短路(因为每条边cost相同，可以BFS)

class Gene:
    def __init__(self, gene:str) -> None:
        self.gene = gene
        self.neighbours = []

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene: return 0
        gene_map = {g:Gene(g) for g in bank}
        gene_list = list(gene_map.values())
        for i in range(0, len(gene_list) - 1):
            for j in range(i + 1, len(gene_list)):
                self.connect(gene_list[i], gene_list[j])
        if endGene not in gene_map:
            return -1
        target = gene_map[endGene]
        start_gene = Gene(startGene)
        for g in gene_list:
            self.connect(start_gene, g)
        vis = set([start_gene])
        q = deque([(start_gene, 0)])
        while q:
            gene, step = q.popleft()
            for n in gene.neighbours:
                if n == target:
                    return step + 1
                if n not in vis:
                    vis.add(n)
                    q.append((n, step + 1))
        return -1

    def connect(self, genx:Gene, geny:Gene) -> None:
        diff = 0
        for i in range(len(genx.gene)):
            if genx.gene[i] != geny.gene[i]:
                diff += 1
                if diff > 1:
                    return
        genx.neighbours.append(geny)
        geny.neighbours.append(genx)

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