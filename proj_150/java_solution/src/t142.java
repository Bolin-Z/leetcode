/* 题目: 120.三角形最小路径和
 * 标签: 
 * 难度: 中等
 * 日期: 1.11
 */

/* 思路:
// 原位修改 对于每一层的节点 i 来说 dp(i) 为到达 i 的最短路径 dp(i) = min(dpj(i-1), dpj(i)) + nums[i] dpj为上一层的dp值
// 直接在 triangle中修改就好
 */

import java.util.List;

public class t142 {
    // 自顶向下
    // public int minimumTotal(List<List<Integer>> triangle) {
    //     int height = triangle.size();
    //     for (int level = 1; level < height; level++){
    //         List<Integer> lastLevel = triangle.get(level - 1);
    //         List<Integer> curLevel = triangle.get(level);
    //         int lastLevelSize = lastLevel.size();
    //         int curLevelSize = curLevel.size();
    //         for(int i = 0; i < curLevelSize; i++){
    //             int len1 = (i - 1 >= 0) ? lastLevel.get(i - 1) : Integer.MAX_VALUE;
    //             int len2 = (i < lastLevelSize) ? lastLevel.get(i) : Integer.MAX_VALUE;
    //             curLevel.set(i, Math.min(len1, len2) + curLevel.get(i));
    //         }
    //     }
    //     int minLen = Integer.MAX_VALUE;
    //     for(int len : triangle.get(height - 1)){
    //         minLen = Math.min(minLen, len);
    //     }
    //     return minLen;
    // }

    // 自底向上
    public int minimumTotal(List<List<Integer>> triangle) {
        for(int i = triangle.size() - 2; i >= 0; i--) {
            // 第 i 行有 i 个元素
            for (int j = 0; j <= i; j++) {
                triangle.get(i).set(j, triangle.get(i).get(j) + Math.min(triangle.get(i+1).get(j), triangle.get(i+1).get(j+1)));
            }
        }
        return triangle.get(0).get(0);
    }
}
