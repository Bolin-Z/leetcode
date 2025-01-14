/* 题目: 70.爬楼梯
 * 标签: 
 * 难度: 简单
 * 日期: 1.10
 */

/* 思路:
// dp[i] = dp[i-1] + dp[i-2]
 */

public class t137 {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        // 从 n = 3 开始
        int dpi_1 = 2;
        int dpi_2 = 1;
        for (int i = 3; i < n; i++){
            int dpi = dpi_1 + dpi_2;
            dpi_2 = dpi_1;
            dpi_1 = dpi;
        }
        return dpi_1 + dpi_2;
    }
}
