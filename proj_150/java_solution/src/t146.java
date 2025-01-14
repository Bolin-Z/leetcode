/* 题目: 97.交错字符串
 * 标签: 
 * 难度: 中等
 * 日期: 1.14
 */

/* 思路:
 * 回溯法? TLE
 * 改进成 dp
 */


public class t146 {
    public static void main(String[] args) {
        t146 solver = new t146();
        String s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac";
        solver.isInterleave(s1, s2, s3);
    }

    // public boolean isInterleave(String s1, String s2, String s3) {
    //     if (s1.length() + s2.length() != s3.length())
    //         return false;
    //     // dp[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符是否可以交错组成 s3 的前 i+j 个字符
    //     boolean[][] dp = new boolean[s1.length() + 1][s2.length() + 1];
    //     // 初始化边界
    //     dp[0][0] = true;
    //     // 初始化第一列
    //     for (int i = 1; i <= s1.length(); i++) {
    //         dp[i][0] = dp[i - 1][0] && s1.charAt(i - 1) == s3.charAt(i - 1);
    //     }
    //     // 初始化第一行
    //     for (int j = 1; j <= s2.length(); j++) {
    //         dp[0][j] = dp[0][j - 1] && s2.charAt(j - 1) == s3.charAt(j - 1);
    //     }
    //     // 递推计算 dp
    //     for (int i = 1; i <= s1.length(); i++) {
    //         for (int j = 1; j <= s2.length(); j++){
    //             dp[i][j] = (dp[i - 1][j] && s1.charAt(i - 1) == s3.charAt(i + j - 1)) || (dp[i][j - 1] && s2.charAt(j - 1) == s3.charAt(i + j - 1));
    //         }
    //     }
    //     return dp[s1.length()][s2.length()];
    // }

    public boolean isInterleave(String s1, String s2, String s3) {
        // 使用滚动数组优化压缩空间
        int m = s1.length(), n = s2.length(), t = s3.length();
        if (m + n != t) return false;
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                // dp[i][j] 只依赖于 dp[i - 1][j] 和 dp[i][j - 1]
                // 因此可以直接使用一维数组 dp[j]
                int p = i + j - 1;
                if (i > 0) dp[j] = dp[j] && s1.charAt(i - 1) == s3.charAt(p);
                if (j > 0) dp[j] = dp[j] || (dp[j - 1] && s2.charAt(j - 1) == s3.charAt(p));
            }
        }
        return dp[n];
    }

    // public boolean isInterleave(String s1, String s2, String s3) {
    //     if (s1.length() + s2.length() != s3.length())
    //         return false;
    //     else
    //         return matches(s3.toCharArray(), s1.toCharArray(), s2.toCharArray(),0, 0, 0);
    // }

    public boolean matches(char[] target, char[] s1, char[] s2, int i, int j, int k) {
        if (i == target.length){
            return true;
        }
        boolean flag;
        // 尝试用 s1 匹配
        flag = j < s1.length && target[i] == s1[j] && matches(target, s1, s2, i + 1, j + 1, k);
        // 尝试用 s2 匹配
        return flag || (k < s2.length && target[i] == s2[k] && matches(target, s1, s2, i + 1, j, k + 1));
    }
}
