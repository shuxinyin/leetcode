class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 类似背包问题
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for x in range(c, amount + 1):
                # 初始化为inf,是为了这里取出min硬币数量
                dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1
