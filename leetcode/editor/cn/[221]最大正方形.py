# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 300 
#  matrix[i][j] 为 '0' 或 '1' 
#  
#  Related Topics 数组 动态规划 矩阵 👍 1208 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''DP
        状态： dp[i][j]是表示以位置（i, j）为右下角的正方形边长。
        转移：   取正方形的四个顶点，进行判断，取min
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        初始化： dp[i][0] = maxtrix[i][0], dp[0][j] = maxtrix[0][j]
        '''

        m, n = len(matrix), len(matrix[0])

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        dp = [[0 for i in range(n)] for j in range(m)]
        # 第一行
        for i in range(m):
            dp[i][0] = matrix[i][0]
        # 第一列
        for j in range(m):
            dp[0][j] = matrix[0][j]

        maxSide = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            maxSide = max(maxSide, dp[i][j])

        return maxSide * maxSide
    # leetcode submit region end(Prohibit modification and deletion)
