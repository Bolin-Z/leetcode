# 题目：274. H指数
# 标签：数组 计数排序 排序
# 难度：中等

from typing import *

# 思路:
# 因为引用范围有限，直接计数排序，然后从最大的引用数目开始，找到一个h使得累加的文章数 >= h

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_possible = min(len(citations), 1024)
        cite_cnt = [0 for _ in range(max_possible)]
        max_cite = 0
        for cite in citations:
            cite_cnt[cite] += 1
            if cite > max_cite:
                max_cite = cite
        h = 0
        sum = 0
        for i in range(max_cite, -1, -1):
            sum += cite_cnt[i]
            if sum >= i:
                h = i
                break
        return h

    def test(self):
        """test code
        """
        test_cases = []
        pass

# 官方题解
# 1. 排序
# 逆序排序，然后遍历下标，递增h，citation[i] > h 说明找到了一篇至少被引用 h + 1 次的论文
# 直到 h 无法增大
def hIndex(self, citations: List[int]) -> int:
    sorted_citation = sorted(citations, reverse = True)
    h = 0; i = 0; n = len(citations)
    while i < n and sorted_citation[i] > h:
        h += 1
        i += 1
    return h 

# 2. 二分搜索
# h 指数的值不可能超过文章发表数，故 h 在区间 [0, n] 二分搜索
def hIndex(self, citations: List[int]) -> int:
    left, right = 0, len(citations)
    while left < right:
        # 猜测h指数的值
        mid = (left + right + 1) >> 1 # 除以2
        cnt = 0
        for v in citations:
            if v >= mid:
                cnt += 1
        if cnt >= mid:
            # 引用数大于 mid 的文章数大于 mid 篇
            # h 指数应当在区间 [mid, right] 内
            left = mid
        else:
            # 引用数大于 mid 的文章数小于 mid 篇
            # h 指数应当在区间 [left, mid) 内
            right = mid - 1
    # left == right
    return left

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()