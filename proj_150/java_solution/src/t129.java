/* 题目: 137.只出现一次的数字II
 * 标签: 
 * 难度:中等
 * 日期:1.9
 */

/* 思路: 状态机的思想 用两个寄存器可以存储某位上1出现的次数 模三 即出现三次时归零
 */


public class t129 {
    public int singleNumber(int[] nums){
        int reg1 = 0;
        int reg2 = 0;
        for (int num : nums) {
            int new_reg1 = (num & ~reg1 & ~reg2) | (~num & reg1);
            int new_reg2 = (num & reg1 & ~reg2) | (~num & reg2);
            reg1 = new_reg1;
            reg2 = new_reg2;
        }
        return reg1;
    }

    public static void main(String[] args) {
        int[] nums = {2,2,3,2};
        t129 solver = new t129();
        solver.singleNumber(nums);
    }
}
