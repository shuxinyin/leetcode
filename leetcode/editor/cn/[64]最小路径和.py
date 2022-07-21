# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 200 
#  0 <= grid[i][j] <= 100 
#  
#  Related Topics 数组 动态规划 矩阵 👍 1296 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''DP
        状态：dp[i][j]表示到达位置（i, j）的总和。
        转移：
            if i == j == 0:  # 初始位置[i][j]
                dp[i][j] = grid[i][j]
            elif i==0:  # 第一行dp[i][j]
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            elif j==0:  # 第一列dp[i][0]
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        初始化： dp = [[0 for _ in range(n)] for _ in range(m)]
        返回： dp[-1][-1]
        '''
        m, n = len(grid), len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == j == 0:  # 位置[i][j]
                    dp[i][j] = grid[i][j]
                elif i==0:  # 第一行dp[i][j]
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j==0:  # 第一列dp[i][0]
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
