class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Space: m*n
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePaths_optimize(self, m: int, n: int) -> int:
        # Space: 2n
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]
        return pre[-1]

    def uniquePaths_optimize2(self, m: int, n: int) -> int:
        # Space: n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # dp[j-1]表示dp[i][j - 1], dp[j]表示dp[i - 1][j]
                cur[j] += cur[j - 1]
            print(cur)

        return cur[-1]


if __name__ == '__main__':
    S = Solution()
    print(S.uniquePaths_optimize2(3, 7))
