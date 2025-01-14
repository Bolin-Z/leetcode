/* 题目: 63.不同路径 II
 * 标签: 
 * 难度: 中等
 * 日期: 1.11
 */

/* 思路: dp[i][j] 为从初始位置到达 (i,j) 的路径数量
//       如果 (i, j) 为障碍物 dp[i][j] = 0
//       如果不为障碍物 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
 */

public class t144 {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        obstacleGrid[0][0] = (obstacleGrid[0][0] == 0) ? 1 : 0;
        for (int i = 0; i < obstacleGrid.length; i++){
            for (int j = 0; j < obstacleGrid[0].length; j++){
                if (i == 0 && j == 0) continue;
                if (obstacleGrid[i][j] == 1){
                    obstacleGrid[i][j] = 0;
                }else{
                    if (i == 0) obstacleGrid[i][j] = obstacleGrid[i][j - 1];
                    else if (j == 0) obstacleGrid[i][j] = obstacleGrid[i - 1][j];
                    else obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j];
                }
            }
        }
        return obstacleGrid[obstacleGrid.length - 1][obstacleGrid[0].length - 1];
    }
}
