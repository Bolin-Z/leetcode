/* 题目: 50.Pow(x,n)
 * 标签: 
 * 难度: 中等
 * 日期: 1.10
 */

/* 思路: 快速幂 将 |n| 转换成二进制表示
 */

public class t135 {
    public double myPow(double x, int n) {
        int pown = Math.abs(n);
        if (pown == 0) return 1.0;
        double res = 1;
        while(pown != 0){
            if((pown & 1) != 0){
                res *= x;
            }
            pown >>>= 1;
            x *= x;
        }
        return n > 0 ? res : 1 / res;
    }

    public double myPow2(double x, int n) {
        // 注意边界条件！n 取绝对值可能溢出 用 long
        double ans = 1;
        long pown = n;
        if (pown < 0){
            pown = -pown;
            x = 1 / x;
        }
        while (n != 0){
            if ((n & 1) == 1){
                ans *= x;
            }
            x *= x;
            pown >>= 1;
        }
        return ans;
    }
}
