# 题目：135. 分发糖果
# 标签：贪心 数组
# 难度：困难

from typing import *

# 思路:
# 记录上一个最高峰值的糖果数
# 记录上一次分配糖果数和评分
# 维护当前下降的长度
# 如果不能赋值 1, 即严格大于则比上一个糖果数 + 1 并更新上一个最高峰值
# 如果可以赋值 1 贪心的赋值 1
#   (1) 和上一个评分相同
#   (2) 比上一个评分低
#       首先要将前 下降步长 个糖果数全部抬高 1 并更新下降步长
#       如果下降步长不小于上一个峰值，说明第一个开始下降的位置已经和峰值一样高了，峰值需要抬高 1

class Solution:
    def candy(self, ratings: List[int]) -> int:
        total_candies = 0
        last_candy = 0
        last_rating = -1
        last_peak = 0
        fall_step = 0
        for r in ratings:
            assign_candy = None
            if r == last_rating:
                assign_candy = 1
                last_peak = 1
                fall_step = 0
            elif r > last_rating:
                assign_candy = last_candy + 1
                last_peak = assign_candy
                fall_step = 0
            else: # r < last_rating
                assign_candy = 1
                total_candies += fall_step
                fall_step += 1
                if last_peak <= fall_step:
                    total_candies += 1
                    last_peak += 1
            last_rating = r
            last_candy = assign_candy
            total_candies += assign_candy

        return total_candies

    def test(self):
        """test code
        """
        test_cases = [
            [1,2,87,87,87,2,1],
            [1,2,3,1,0],
            [1,3,2,2,1],
            [1,0,2],
            [1,2,2]
        ]
        for i, case in enumerate(test_cases):
            self.candy(case)

# 官方题解
# 补充方法
# 两次遍历 + 额外空间
# 左规则： ratings[i - 1] < rating[i] i 比 i - 1 多
# 右规则： ratings[i] > rating[i + 1] i 比 i + 1 多
# 左右个遍历一次，每人分得的最少糖果为上述两个规则的最大值

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        # 用一个变量去维护右规则更新即可
        right = answer = 0
        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            # 选择最大的数值
            # answer += max(candies[i], right)
            # 优化 用 sum 比较快
            candies[i] = max(candies[i], right)
        return sum(candies)
            

# 测试
if __name__ == "__main__":
    solver = Solution()
    solver.test()