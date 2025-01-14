/* 题目: 188.买卖股票的最佳时机 IV
 * 标签: 
 * 难度: 困难
 * 日期: 1.14
 */

/* 思路:
 */

import java.util.Arrays;

public class t149 {
    public int maxProfit(int k, int[] prices) {
        return dp(k, prices);
    }

    // 递归写法
    public int dfs(int[] prices, int date, int k, boolean hold){
        if (k < 0) return Integer.MIN_VALUE;
        if (date < 0) return hold ? Integer.MIN_VALUE : 0;
        if (hold) {
            return Math.max(dfs(prices, date - 1, k, true), dfs(prices, date - 1, k, false) - prices[date]);    
        } else {
            return Math.max(dfs(prices, date - 1, k, false), dfs(prices, date - 1, k - 1, true) + prices[date]);
        }
    }

    // dp 写法
    public int dp(int k, int[] prices) {
        int n = prices.length;
        int [][][] f = new int[n + 1][k + 2][2];
        for (int[][] mat : f) {
            for (int[] row : mat) {
                Arrays.fill(row, Integer.MIN_VALUE >> 1);
            }
        }
        for (int j = 1; j <= k + 1; j++) {
            f[0][j][0] = 0;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= k + 1; j++) {
                f[i + 1][j][0] = Math.max(f[i][j][0], f[i][j][1] + prices[i]);
                f[i + 1][j][1] = Math.max(f[i][j][1], f[i][j - 1][0] - prices[i]);
            }
        }
        return f[n][k + 1][0];
    }
}
