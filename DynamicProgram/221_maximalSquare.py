class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 状态dp[i][j]表示以[i, j]为右下角的正方形（只包含1）的边长最大值
        # 转移： dp[i, j] = min(dp[i-1,j], dp[i-1, j-1], dp[i, j-1]) + 1
        # 初始状态： dp[0,j]=mat[0, j], dp[i,0]=mat[i,0]
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        maxSquare = maxSide * maxSide
        return maxSquare
