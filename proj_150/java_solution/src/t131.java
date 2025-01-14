/* 题目: 9.回文数
 * 标签: 
 * 难度: 简单
 * 日期: 1.9
 */

/* 思路: <0 就肯定不是回文数
 */

public class t131 {
    public boolean isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        int high_mask = 1;
        while(x / high_mask > 9){
            high_mask *= 10;
        }
        while(x != 0){
            int high_digit = x / high_mask;
            int low_digit = x % 10;
            if(high_digit != low_digit){
                return false;
            }
            x = (x % high_mask) / 10;
            high_mask /= 100;
        }
        return true;
    }

    public boolean isPalindromeAns(int x){
        // 对数字的后半部分进行反转 边反转边和前半部分比较
        if (x < 0 || (x % 10 == 0) && x != 0){
            // 小于0 和个位为0且不等于0 的数不为回文数
            return false;
        }
        int revertedNumber = 0;
        while (x > revertedNumber){
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        // 分别为长度是奇数和偶数时的情况
        return x == revertedNumber || x == revertedNumber / 10;
    }

    public static void main(String[] args) {
        t131 solver = new t131();
        solver.isPalindrome(12321);
    }
}
