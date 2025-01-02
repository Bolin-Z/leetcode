# 题目：502.IPO
# 标签：贪心 数组 排序 堆(优先队列)
# 难度：困难
# 日期：1.1

from typing import *
from heapq import *

# 思路:
# 贪心的选择当前可以选择的最大利润的项目
# 先根据资本对所有任务进行升序排序
# 将当前可以投资的所有项目根据利润加入一个优先队列
# 然后选取一个最大利润的

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        pro_cap = [(profits[i], capital[i])for i in range(n)]
        pro_cap.sort(key=lambda t:t[1]) # 按照资金升序排序
        pq = []
        ans, project_nums, idx = w, min(k, n), 0
        while idx < n:
            pro, cap = pro_cap[idx]
            if cap > ans:
                break
            heappush(pq, - pro)
            idx += 1
        while project_nums and pq: # 还可以做项目
            pro = - heappop(pq)
            ans += pro # 做该项目
            while idx < n: # 加入可以做的项目
                pro, cap = pro_cap[idx]
                if cap > ans:
                    break
                heappush(pq, -pro)
                idx += 1
            project_nums -= 1
        return ans

    def test(self):
        k = 2
        w = 0
        profits =[1,2,3]
        captital = [0,1,1]
        self.findMaximizedCapital(k, w, profits, captital)


# 官方题解
# 简洁写法
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))
        n = len(profits)
        curr = 0
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort(key=lambda x:x[0])

        pq = []
        for _ in range(k):
            while curr < n and arr[curr][0] <= w:
                heappush(pq, -arr[curr][1])
                curr += 1
            
            if pq:
                w -= heappop(pq)
            else:
                break
        return w

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()