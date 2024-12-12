# 题目：121. 买卖股票的最佳时机
# 标签：数组 动态规划
# 难度：简单

from typing import *

# 思路:
# 前 i 天能获取的最大利润 = max {今天卖出 - 前 i - 1 天最低价格时买入, 前i - 1天卖出的最低价格}
# dp[i] = max{cur_price - cur_low, dp[i - 1]}
# dp[last_day] 为最终答案

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_lowest = prices[0]
        for price in prices:
            if price - cur_lowest > max_profit:
                max_profit = price - cur_lowest
            if price < cur_lowest:
                cur_lowest = price
        return max_profit


# 官方题解