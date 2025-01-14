/* 题目: 64.最小路径和
 * 标签: 
 * 难度: 中等
 * 日期: 1.11
 */

/* 思路: d[i][j] 为从左上角出发到 (i,j) 的最短路径
//      只能向右或向下移动, 所以 d[i][j] = min(d[i-1][j], d[i][j-1]) + grid[i][j]
//      直接在grid上修改就好
 */

public class t143 {
    public int minPathSum(int[][] grid) {
        // int m = grid.length;
        // int n = grid[0].length;
        // for(int j = 1;j < n; j++){
        //     grid[0][j] += grid[0][j - 1];
        // }
        // for(int i = 1; i < m; i++){
        //     for(int j = 0; j < n; j++){
        //         grid[i][j] += (j == 0) ? grid[i - 1][j] : Math.min(grid[i - 1][j], grid[i][j - 1]);
        //     }
        // }
        // return grid[m - 1][n - 1];

        // 边界处理
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (i == 0 && j == 0) continue;
                else if (i == 0) grid[i][j] += grid[i][j - 1];
                else if (j == 0) grid[i][j] += grid[i - 1][j];
                else grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);
            }
        }
        return grid[grid.length - 1][grid[0].length - 1];
    }
}
