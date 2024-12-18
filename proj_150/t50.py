# 题目：57.插入区间
# 标签：数组
# 难度：中等
# 日期：12.18

from typing import *

# 思路:
# t49 56.合并区间 升级版本

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        idx, is_added = 0, False
        while idx < len(intervals):
            # 下一个要处理的区间
            process = intervals[idx]
            if not is_added and newInterval[0] <= process[0]:
                process = newInterval
                idx -= 1
                is_added = True
            if answer and process[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], process[1])
            else:
                answer.append(process)
            idx += 1
        if not is_added:
            if answer and newInterval[0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], newInterval[1])
            else:
                answer.append(newInterval)
        return answer

    def test(self):
        """test code
        """
        test_cases = []
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = []
            if type(answer) == List:
                for ans in answer:
                    print(f"\t\t{ans}")
            else:
                print(f"\t\t{answer}")

# 官方题解

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()