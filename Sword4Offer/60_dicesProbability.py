class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        # Time: O(n^2)
        # Space: O(n)
        dp = [1 / 6] * 6
        for i in range(2, n + 1):
            tmp_dp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp_dp[j + k] += dp[j] / 6
            dp = tmp_dp
        return dp
