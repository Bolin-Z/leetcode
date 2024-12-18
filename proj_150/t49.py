# 题目：56. 合并区间
# 标签：数组 排序
# 难度：中等
# 日期：12.18

from typing import *

# 思路:
# 先按照左区间排序，再用分组循环

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals = sorted(intervals, key= lambda interval:interval[0])
        i, n =0, len(intervals)
        while i < n:
            left_most, right_most = intervals[i][0], intervals[i][1]
            while i < n - 1 and intervals[i + 1][0] <= right_most:
                right_most = max(right_most, intervals[i+1][1])
                i += 1
            answer.append([left_most, right_most])
            i += 1
        return answer

    def test(self):
        """test code
        """
        test_cases = [
            [[[2,3],[4,5],[6,7],[8,9],[1,8]]],
            [[[1,3],[2,6],[8,10],[15,18]]]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.merge(case[0])
            if type(answer) == List:
                for ans in answer:
                    print(f"\t\t{ans}")
            else:
                print(f"\t\t{answer}")

# 官方题解
# 灵山
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort(key=lambda p : p[0])
        for p in intervals: # 当前正在处理第 p 个区间
            if answer and p[0] <= answer[-1][1]:
                # 先保证answer非空 answer最后一个区间为正在操作的区间
                answer[-1][1] = max(answer[-1][1], p[1]) # 扩充右边界
            else: # 不相交 answer中最后一个区间处理完毕 加入新的待处理区间
                answer.append(p)
        return answer

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()