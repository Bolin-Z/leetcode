/* 题目: 300.最长递增子序列 *
 * 标签: 数组 二分查找 动态规划
 * 难度: 中等
 * 日期: 1.10
 */

/* 思路: 用一个数组 g[i] 存储 长度为 i + 1 的子序列中 末尾最小的元素值, 可以用反证法证明 g 是一个单调递增数组
// g.length() 为当前的最长递增子序列长度, 对于一个新加入的元素 num , 如果 num > g[g.length - 1] 说明找到了一个更长的递增子序列将其加入g末尾
// 否则 则使用二分查找在g中找到一个位置 j s.t. g[j-1] < num <= g[j] 更新 g[j] = num
// 内存优化: 直接使用nums数组来作为 g (遍历过的元素就不需要了)
// 
// 有用的博客
// https://writings.sh/post/longest-increasing-subsequence-revisited#footnote-1 
*/

public class t141 {
    public int lengthOfLIS(int[] nums) {
        int ng = 1;
        for (int i = 1; i < nums.length; i++){
            int num = nums[i];
            if (num > nums[ng - 1]){
                nums[ng] = num;
                ng += 1;
            }else{
                int j = lowerBound(nums, ng, num);
                nums[j] = num;
            }
        }
        return ng;
    }

    private int lowerBound(int[] g, int g_size, int num){
        int left = 0;
        int right = g_size - 1;
        while (left <= right) {
            // 循环不变式
            // left - 1 及之前的 j  : g[j] < num
            // right + 1 及之后的 j : g[j] >= num
            int mid = left + (right - left) / 2;
            if (g[mid] == num){
                return mid;
            }else if(g[mid] < num){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return left;
    }
}
