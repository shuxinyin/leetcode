class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 类似完全背包问题
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for x in range(c, amount + 1):
                # 初始化为inf,是为了这里取出min硬币数量
                dp[x] += dp[x - c]
            # print(dp)
        return dp[-1]