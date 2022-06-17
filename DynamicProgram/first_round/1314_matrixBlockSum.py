class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(m * n * min(m, n))
        # Space: O(m * n)
        m, n = len(mat), len(mat[0])

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for x in range(1, m + 1):
            for y in range(1, n + 1):
                dp[x][y] = dp[x][y - 1] + dp[x - 1][y] - dp[x - 1][y - 1] + mat[x - 1][y - 1]

        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return dp[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + k + 1, j + k + 1) - get(i - k, j + k + 1) - \
                            get(i + k + 1, j - k) + get(i - k, j - k)
        return ans

