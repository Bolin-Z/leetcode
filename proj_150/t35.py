# 题目：54.螺旋矩阵
# 标签：数组 矩阵 模拟
# 难度：中等
# 日期：

from typing import *

# 思路:
# 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        y, x = 0, 0
        bl, bu, br, bd = -1, -1, len(matrix[0]), len(matrix)
        RIGHT, LEFT, DOWN, UP = 0, 1, 2, 3
        state = RIGHT
        total_nums = len(matrix) * len(matrix[0])
        while len(answer) < total_nums:
            answer.append(matrix[y][x])
            # move
            if state == RIGHT:
                if not x + 1 < br:
                    bu += 1
                    state = DOWN
                    y += 1
                else: x += 1
            elif state == LEFT:
                if not x - 1 > bl:
                    bd -= 1
                    state = UP
                    y -= 1
                else: x -= 1
            elif state == DOWN:
                if not y + 1 < bd:
                    br -= 1
                    state = LEFT
                    x -= 1
                else: y += 1
            else:
                if not y - 1 > bu:
                    bl += 1
                    state = RIGHT
                    x += 1
                else: y -= 1
        return answer

    def test(self):
        """test code
        """
        test_cases = [
            [[1,2,3],[4,5,6],[7,8,9]]
        ]
        for i, case in enumerate(test_cases):
            print(f"测试用例 {i + 1}")
            print(f"\t输入:")
            for item in case:
                print(f"\t\t{item}")
            print(f"\t输出:")
            # 调用求解函数
            answer = self.spiralOrder(case)
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