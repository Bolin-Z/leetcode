# 题目：452.用最少数量的箭引爆气球
# 标签：贪心 数组 排序
# 难度：中等
# 日期：12.18

from typing import *
from math import inf

# 思路:
#

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p:p[0])
        rightmost, cnt = inf, 0
        for p in points:
            if rightmost < inf and p[0] <= rightmost:
                rightmost = min(rightmost, p[1])
            else:
                cnt += 1
                rightmost = p[1]
        return cnt

    def test(self):
        """test code
        """
        test_cases = [
            [[[10,16],[2,8],[1,6],[7,12]]]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.findMinArrowShots(case[0])
            if type(answer) == List:
                for ans in answer:
                    print(f"\t\t{ans}")
            else:
                print(f"\t\t{answer}")

# 官方题解
# 灵山 将区间按照右端点升序排序
# 遍历 可知右端点单调不减 如果左端点小于当前最小右端点 则已经包含点，跳过
# 如果左端点大于，则要重新放点
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p:p[1])
        ans, pre = 0, -inf # 点数和上一个放点位置
        for p in points:
            if p[0] > pre:
                ans += 1
                pre = p[1]
        return ans


# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()