/* 题目: 198.打家劫舍
 * 标签: 
 * 难度: 中等
 * 日期: 1.10
 */

/* 思路:
// dp[i]: 偷前i家能得到的最大值
// dp[i] = max(dp[i-1], dp[i-2] + nums[i])
//
// 补充解释
//
// dp[i][1] 表示偷第i间房的最大金额 dp[i][0] 表示不偷这间房的最大金额
// 递推关系
//   1.dp[i][1] = dp[i-1][0] + nums[i]
//   2.dp[i][0] = max(dp[i-1][0], dp[i-1][1])
//
// 定义dp[i] 为偷到第i间房的最大金额
// 则有 dp[i][0] = dp[i-1] 不偷第i间房的最大金额等于偷到第i间房的最大值
// 则对于 1 2 式有
//   1.dp[i][1] = dp[i-1][0] + nums[i] = dp[i-2] + nums[i]
//   2.dp[i][0] = dp[i-1]
// dp[i] = max(dp[i][1], dp[i][0]) = max(dp[i-2] + nums[i], dp[i-1])
*/

public class t138 {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        int dpi_1 = Math.max(nums[0], nums[1]);
        int dpi_2 = nums[0];
        for (int i = 2; i < n; i++){
            int dpi = Math.max(dpi_1, dpi_2 + nums[i]);
            dpi_2 = dpi_1;
            dpi_1 = dpi;
        }
        return dpi_1;
    }

    public static void main(String[] args) {
        t138 solver = new t138();
        int[] nums = {1,2,3,1};
        solver.rob(nums);
    }
}
