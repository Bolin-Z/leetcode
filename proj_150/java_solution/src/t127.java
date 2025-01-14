/* 题目: 191.位1的个数
 * 标签: 
 * 难度: 简单
 * 日期: 1.2
 */

/* 思路:
   采用分治法 同 t126 190
   32位数的1的个数等于前16和后16里1的数目
   16 前 8 后 8
   8 前 4 后 4
   4 前 2 后 2
   2 前 1 后 1
   直接相加
 */

public class t127 {
    final private static int M1 = 0x55555555;
    final private static int M2 = 0x33333333;
    final private static int M3 = 0x0f0f0f0f;
    final private static int M4 = 0x00ff00ff;
    final private static int M5 = 0X0000ffff;

    public int hammingWeight(int n) {
        n = (n & M1) + ((n >>> 1) & M1); // 将 奇偶位上的1相加,用2bit表示总数目(>2)
        n = (n & M2) + ((n >>> 2) & M2); // 将2bit看作一个整体 前后相加
        n = (n & M3) + ((n >>> 4) & M3);
        n = (n & M4) + ((n >>> 8) & M4);
        n = (n & M5) + ((n >>> 16) & M5);
        return n;   
    }
}
