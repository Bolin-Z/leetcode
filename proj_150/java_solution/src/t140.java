/* 题目: 322.零钱兑换
 * 标签: 
 * 难度: 中等
 * 日期: 1.10
 */

/* 思路:
// dp[i] = min(dp[i - k]) + 1 forall k in coins
 */

import java.util.Arrays;

public class t140 {
    class Solution {
        public int coinChange(int[] coins, int amount) {
            int[] dp = new int[amount + 1];
            Arrays.fill(dp, -1);
            dp[0] = 0;
            for(int i = 1;i <= amount; i++){
                int minCoinNum = Integer.MAX_VALUE;
                for (int coin : coins){
                    if (i - coin >= 0 && dp[i - coin] != -1){
                        minCoinNum = Math.min(minCoinNum, dp[i - coin]);
                    }
                }
                if (minCoinNum != Integer.MAX_VALUE){
                    dp[i] = minCoinNum + 1;
                }
            }
            return dp[amount];
        }
    }    
}
