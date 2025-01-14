/* 题目:136.只出现一次的数字
 * 标签: 
 * 难度:简单
 * 日期:1.3
 */

/* 思路:
   直接异或操作
 */

public class t128 {
    public int singleNumber(int[] nums) {
        int n = 0;
        for (int i = 0; i < nums.length; i++) {
            n ^= nums[i];
        }
        return n;
    }
}
