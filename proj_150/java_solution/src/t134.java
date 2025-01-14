/* 题目: 69.x的平方根
 * 标签: 
 * 难度: 简单
 * 日期: 1.9
 */

/* 思路: 二分查找
 */

public class t134 {
    public int mySqrt(int x) {
        if (x <= 1){
            return x;
        }
        int left = 1;
        int right = x / 2;
        while (left <= right){
            // 对 left - 1 的所有数有 i ** 2 < x
            // 对 right + 1 的所有数有 i ** 2 > x
            int mid = left + (right - left) / 2;
            long sqMid = (long)mid * (long)mid;
            if (sqMid == x){
                return mid;
            }else if(sqMid < x){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return right;
    }

    public static void main(String[] args) {
        t134 solver = new t134();
        solver.mySqrt(2147395599);
    }
}
