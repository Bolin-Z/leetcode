/* 题目: 149. 直线上最多的点数
 * 标签: 
 * 难度: 困难
 * 日期: 1.10
 */

/* 思路: 两点确定一条直线 每个点两两之前确定一条直线的参数值
         参数值相同则在一条直线上
 */

import java.util.HashMap;

public class t136 {
    private final int SHIFT = 20001;
    public int maxPoints(int[][] points) {
        int n = points.length;
        if (n <= 2) return n;
        int res = 0;
        for(int i = 0; i < n; i++){
            // 优化：如果剩下的点数小于等于当前最优解，直接返回
            if (res >= n - i) break;
            int x1 = points[i][0];
            int y1 = points[i][1];
            HashMap<Integer, Integer> cnt = new HashMap<>();
            for(int j = i + 1; j < n; j++){
                int x2 = points[j][0];
                int y2 = points[j][1];
                int hashCode = getHash(y2 - y1, x2 - x1);
                cnt.put(hashCode, cnt.getOrDefault(hashCode, 1) + 1);
            }
            for (int c: cnt.values()){
                res = Math.max(c, res);
            }
        }
        return res;
    }

    private int gcd(int a, int b) {
        if (a == 1 || b == 1) return 1;
        while(b > 0){
            int tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }

    /* 对于斜率为dy/dx的直线，我们可以用一个hash值来表示，hash值为dy * SHIFT + dx */
    private int getHash(int dy, int dx) {
        if (dy == 0) return 0;
        if (dx == 0) return Integer.MAX_VALUE;
        int sign = dy * dx > 0 ? 1 : -1;
        dy = Math.abs(dy);
        dx = Math.abs(dx);
        int g = gcd(dy, dx);
        dy /= g;
        dx /= g;
        return sign * (dy * SHIFT + dx);
    }
}
