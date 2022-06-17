class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        n = len(triangle)

        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(0, i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]


    def minimumTotal_optimize(self, triangle: [[int]]) -> int:
        # 优化空间 O(n)
        n = len(triangle)

        dp = [0 for i in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(0, i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]
