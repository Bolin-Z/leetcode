# 题目：373.查找和最小的k对数字
# 标签：数组 堆(优先队列)
# 难度：中等
# 日期：1.1

from typing import *
from heapq import *

# 思路:
# 使用一个优先队列 对于数对 (u,v) 来说 其之后最小的数可能为 (u + 1,v) 或 (u,v + 1)

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        heapify(pq)
        for _ in range(k):
            if pq: # 还有元素
                _, i, j = heappop(pq)
                ans.append([nums1[i], nums2[j]])
                if j + 1 < n:
                    j = j + 1
                    heappush(pq, (nums1[i] + nums2[j], i, j))
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