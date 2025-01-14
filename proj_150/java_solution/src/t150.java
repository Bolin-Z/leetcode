/* 题目: 221.最大正方形
 * 标签: 
 * 难度: 中等
 * 日期: 1.14
 */

/* 思路:
 * dp[i][j] 以 (i,j)为右下角顶点的最大正方形的边长
 */

public class t150 {
    public int maximalSquare(char[][] matrix) {
        int maxSide = 0;
        int m = matrix.length, n = matrix[0].length;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++){
            for (int j = 1; j <= n; j++){
                if (matrix[i - 1][j - 1] == '1') {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i][j - 1], dp[i - 1][j])) + 1;
                    maxSide = Math.max(maxSide, dp[i][j]);
                }
            }
        }
        return maxSide * maxSide;
    } 
}
