/* 题目: 172.阶乘后的零
 * 标签: 
 * 难度: 中等
 * 日期: 1.9
 */

/* 思路: 分析 n! 中质因子5的个数
 */

public class t133 {
    public int trailingZeroes(int n) {
        int ans = 0;
        while(n != 0){
            n /= 5;
            ans += n;
        }
        return ans;
    }
}
