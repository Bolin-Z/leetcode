# 题目：122. 买卖股票的最佳时机
# 标签：贪心 数组 动态规划
# 难度：中等

from typing import *
from math import inf

# 思路:
# 具有贪心的性质，最优子结构，因为可以无限次交易
# 将每天的价格表示成图表
# 输入 [7,1,5,3,6,4]
#
# +
# +       +
# +   +   +
# +   +   + +
# +   + + + +
# +   + + + +
# + + + + + +
#
# 找到所有上坡，将上坡累加，局部最优叠加就是全局最优
# 假设有个两个上升，可以拆分成两个，一定不差于合并起来

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
        return profit

# 官方题解
# 补充动态规划解法
# 定义状态
# dp[i][0]：第i天交易完后手里没有股票最大利润
# dp[i][1]：第i天交易完后手里持有股票最大利润
# 状态转移方程
# 手里没有股票：第 i - 1 天手里没有股票 或 第 i - 1 天手里持有一只股票，并将其卖出(卖出获得prices[i])
# dp[i][0] = max{dp[i - 1][0], dp[i - 1][1] + prices[i]}
# 手里持有股票：第 i - 1 天手里有股票 或 第 i - 1 天手里没有，今天买入(买入减少prices[i])
# dp[i][1] = max{dp[i - 1][1], dp[i-1][0] - prices[i]}

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0
        dp1 = -inf
        for p in prices:
            new_dp0 = max(dp0, dp1 + p)
            new_dp1 = max(dp1, dp0 - p)
            dp0 = new_dp0
            dp1 = new_dp1
        return dp0