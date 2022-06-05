class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # 表示最差情况下的数量，如 i=4，最坏结果为 4=1+1+1+1 即为 4 个数字
            dp[i] = i

            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]
