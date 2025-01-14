/* 题目: 190.颠倒二进制位
 * 标签: 位运算 分治
 * 难度: 简单
 * 日期: 1.2
 */

/* 思路:
 *   分治法 分成前后两部分 然后 分别颠倒 再把颠倒后的两部分整体拼接
 *   32 位 前16和后16
 *   16    前8后8
 *   8     前4后4
 *   4     前2后2
 *   2     前后交换 边界
 */


public class t126 {
    final private static int M1 = 0x55555555;
    final private static int M2 = 0x33333333;
    final private static int M3 = 0x0f0f0f0f;
    final private static int M4 = 0x00ff00ff;
    final private static int M5 = 0X0000ffff;
    public int reverseBits(int n) {
        n = (n & M1) << 1 | (n >>> 1) & M1;
        n = (n & M2) << 2 | (n >>> 2) & M2;
        n = (n & M3) << 4 | (n >>> 4) & M3;
        n = (n & M4) << 8 | (n >>> 8) & M4;
        n = (n & M5) << 16 | (n >>> 16) & M5;
        return n;
    }
}
