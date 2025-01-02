# 题目：295.数据流的中位数
# 标签：设计 双指针 数据流 排序 堆(优先队列)
# 难度：困难
# 日期：1.2

from typing import *
from heapq import *

# 思路:
# 维护两个优先队列
# 一个最大堆一个最小堆
# 假设当前有 n 个数 最大堆存放前 (n + 1) // 2 个 最小堆存放后面的

class MedianFinder:

    def __init__(self):
        self.first_half = [] # 前半部分用最大堆 记得取反
        self.second_half = [] # 后边部分用最小堆
        self.total_num = 0

    def addNum(self, num: int) -> None:
        if not self.first_half or -self.first_half[0] >= num:
            # 第一部分为空 或 大于等于第一部分所有数
            heappush(self.first_half, -num)
            if len(self.first_half) > len(self.second_half) + 1: # 超出数量
                item = - heappop(self.first_half)
                heappush(self.second_half, item)
        else: # 加入第二部分
            heappush(self.second_half, num)
            if len(self.second_half) > len(self.first_half): # 超出数量
                item = heappop(self.second_half)
                heappush(self.first_half, -item)
        self.total_num += 1

    def findMedian(self) -> float:
        return -self.first_half[0] if self.total_num % 2 else (self.second_half[0] - self.first_half[0]) / 2

class Solution:
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
# 简洁写法
class MedianFinder:

    def __init__(self):
        self.first_half = [] # 前半部分用最大堆 记得取反
        self.second_half = [] # 后边部分用最小堆

    def addNum(self, num: int) -> None:
        # 始终保持 前半部分长度最多大于后半 1 最小相等
        if len(self.first_half) == len(self.second_half):
            heappush(self.first_half, - heappushpop(self.second_half, num))
        else:
            heappush(self.second_half, -heappushpop(self.first_half, -num))

    def findMedian(self) -> float:
        return -self.first_half[0] if len(self.first_half) > len(self.second_half) else \
            (self.second_half[0] - self.first_half[0]) / 2
# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()