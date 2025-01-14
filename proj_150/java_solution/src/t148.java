/* 题目: 123. 买卖股票的最佳时机 III
 * 标签: 
 * 难度: 困难
 * 日期: 1.14
 */

/* 思路:
 */

import java.util.Arrays;

public class t148 {
    public int maxProfit(int[] prices) {
        return dp(2, prices);
    }

    public int dp(int maxK, int[] prices) {
        int n = prices.length;
        int [][][] f = new int[n + 1][maxK + 2][2];
        for (int[][] mat : f) {
            for (int[] row : mat) {
                Arrays.fill(row, Integer.MIN_VALUE >> 1);
            }
        }
        for (int j = 1; j <= maxK + 1; j++) {
            f[0][j][0] = 0;
        }
        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= maxK + 1; j++) {
                f[i + 1][j][0] = Math.max(f[i][j][0], f[i][j][1] + prices[i]);
                f[i + 1][j][1] = Math.max(f[i][j][1], f[i][j - 1][0] - prices[i]);
            }
        }
        return f[n][maxK + 1][0];
    }
}
