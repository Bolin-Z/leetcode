/* 题目:201.数字范围按位与
 * 标签: 
 * 难度:中等
 * 日期:1.9
 */

/* 思路: 暴力解法 一直按位与
         在与运算中只要有0就肯定一直保持0,从左往右看,第一位出现不同的位,及之后需要置0
 */

public class t130 {
    public int rangeBitwiseAnd(int left, int right) {
        int xor = left ^ right;
        int mask = 0x80000000;
        int bit_length = 32;
        while(mask != 0 && (xor & mask) == 0){
            mask >>>= 1;
            bit_length -= 1;
        }
        return left & (~((1<<bit_length) - 1));
    }

    public static void main(String[] args) {
        t130 solver = new t130();
        solver.rangeBitwiseAnd(5, 7);
    }
}
