# 题目：134. 加油站
# 标签：贪心 数组
# 难度：中等

from typing import *
from math import inf

# 思路:
# 将 gas 和 cost 作差，差值意为通过后的油量变化
# 如果所有油量变化加起来 < 0 肯定无解
# 总油量变化 > 0 时有解
# 贪心找最多油量变化的那个点就好 (不太对) 有可能没到达下一个正的就无了
# 从前往后，第一个能够到达最后一个点的

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_sum = 0
        candidate = None
        cur_sum = 0
        for i in range(len(gas)):
            delta = gas[i] - cost[i]
            total_sum += delta
            if candidate != None: # 直接用 if candidate 会出错，因为 candidate == 0 时也会为false
                cur_sum += delta
                if cur_sum < 0:
                    candidate = None
                    cur_sum = 0
            else:
                if delta >= 0:
                    candidate = i
                    cur_sum = delta
        if total_sum < 0:
            return -1
        else:
            return candidate

    def test(self):
        """test code
        """
        test_cases = [
            [
                [1,2,3,4,5], [3,4,5,1,2]
            ],
            [
                [5,8,2,8], [6,5,6,6]
            ],
            [
                [2,0,1,2,3,4,0], [0,1,0,0,0,0,11]
            ]
        ]
        for i, c in enumerate(test_cases):
            print(f"case: {i}")
            print(f"\t input: gas  = {c[0]}")
            print(f"\t        cost = {c[1]}")
            print(f"\t output: {self.canCompleteCircuit(c[0], c[1])}")
# 官方题解
# 假设从x出发，每经过一个加油站就加一次油，最后一个可以到达的加油站是y（假设x < y）
# 则有
# sum_{i=x to y} gas[i] < sum_{i=x to y} cost[i] （cost[y] 为从 y 到 y + 1 的消耗，到达不了）
# sum_{i=x to j} gas[i] >= sum_{i=x to j} cost[i] for all j in [x,y)
# 进一步，对于 x, y 之间的 任意加油站 z 有
# sum_{i=z to y} gas[i] = sum_{i=x to y} gas[i] - sum_{i=x to z-1} gas[i]
#                       < sum_{i=x to y} cost[i] - sum_{i=x to z-1} gas[i] （上式1）
#                       < sum_{i=x to y} cost[i] - sum_{i=x to z-1} cost[i] （上式2）
#                       = sum_{i=z to y} cost[i]
# 即从 z 也无法到达 y + 1
# 从 0 号加油站开始，判断是否能够环绕一周，不能就从第一个无法到达的加油站开始继续检查

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            sum_of_gas = sum_of_cost = 0
            cnt = 0
            while cnt < n:
                j = (i + cnt) % n
                sum_of_gas += gas[j]
                sum_of_cost += cost[j]
                if sum_of_cost > sum_of_gas:
                    break
                cnt += 1
            if cnt == n: # 可以遍历
                return i
            else: # 第一个不能到达的节点
                i += cnt + 1
        return -1 # 没有符合要求的点

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()