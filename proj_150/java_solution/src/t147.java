/* 题目: 72.编辑距离
 * 标签: 
 * 难度: 中等
 * 日期: 1.14
 */

/* 思路:
 * 最长公共子序列？LCS (不太正确)
 * 子序列是不需要变的部分
 * 其他部分通过 增删改 来实现
 * 使用动态规划求解
 * dp[i][j] 表示 word1 的前 i 个字符和 word2 的 前 j 个字符的最长公共子序列
 * 1. 如果 word1[i] == word2[j] 那么 dp[i][j] = dp[i - 1][j - 1] + 1
 * 2. 如果 word1[i] != word2[j] 那么 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
 * 
 * 稍微修改一下
 * 往一个字符串插入字符等价于从另一个字符串删除字符
 * 统一视为插入
 * dp[i][j] 表示 word1 的前 i 个字符和 word2 的 前 j 个字符的最小编辑距离
 * 1. 如果 word1[i] == word2[j] 那么 dp[i][j] = dp[i - 1][j - 1]
 * 2. 如果 word1[i] != word2[j] 那么 dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
 *   2.1 dp[i - 1][j - 1] 通过替换最后一个字符
 *   2.2 dp[i - 1][j] 通过往 word1[0:i-1] 末尾插入一个字符
 *   2.3 dp[i][j - 1] 通过往 word2[0:j-1] 末尾插入一个字符
 */

public class t147 {
    public static void main(String[] args) {
        t147 solution = new t147();
        String word1 = "intention", word2 = "execution";
        System.out.println(solution.minDistance(word1, word2));
    }

    public int minDistance(String word1, String word2) {
        char [] s1 = word1.toCharArray(), s2 = word2.toCharArray();
        int m = s1.length, n = s2.length;
        int [][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1])) + 1;
                }
            }
        }
        return dp[m][n];
    }

    // public int LCS(char[] s1, char[] s2) {
    //     int m = s1.length, n = s2.length;
    //     int [][] dp = new int[m + 1][n + 1];
    //     // 初始化
    //     // 默认赋值为 0 省略
    //     for (int i = 1; i <= m; i++) {
    //         for (int j = 1; j <= n; j++) {
    //             dp[i][j] = (s1[i - 1] == s2[j - 1]) ? dp[i - 1][j - 1] + 1 : Math.max(dp[i - 1][j], dp[i][j - 1]);
    //         }
    //     }
    //     return dp[m][n];
    // }
}
