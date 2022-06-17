class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        n = len(cost)
        dp = [0] * len(cost)
        dp[1] = min(cost[0], cost[1])
        for i in range(2, n):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i - 1])
        return dp[-1]

    def minCostClimbingStairs2(self, cost: [int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        print(dp)
        for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
        print(dp)

        return min(dp[-2], dp[-1])


if __name__ == '__main__':
    S = Solution()
    print(S.minCostClimbingStairs2([10, 15, 20]))
