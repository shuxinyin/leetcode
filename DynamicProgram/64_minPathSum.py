class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                elif i==0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j==0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    mat = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

    S =Solution()
    print(S.minPathSum(grid=mat))