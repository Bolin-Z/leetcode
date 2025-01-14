/* 题目: 66.加一
 * 标签: 
 * 难度: 简单
 * 日期: 1.9
 */

/* 思路:
 */

public class t132 {
    public int[] plusOne(int[] digits) {
        int carry_bit = 1;
        for(int i = digits.length - 1;i >= 0;i--){
            int tmp = digits[i] + carry_bit;
            digits[i] = tmp % 10;
            carry_bit = tmp / 10;
        }
        int[] result = digits;
        if (carry_bit != 0){
            result = new int[digits.length + 1];
            result[0] = 1;
            for(int i = 0; i < digits.length; i++){
                result[i + 1] = digits[i];
            }
        }
        return result;
    }
    public int[] plusOneAns(int[] digits){
        // 从低位到高位开始判断,每一位+1后是否为0不为0就结束,为0就继续
        int len = digits.length;
        for (int i = len - 1; i >= 0; i--) {
            digits[i] = (digits[i] + 1) % 10;
            if (digits[i] != 0){
                // 不会再有进位
                return digits;
            }
        }
        // 位数增加, 且原本数字为99999...
        digits = new int[len + 1];
        digits[0] = 1;
        return digits;
    }
}
