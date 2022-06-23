# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。 
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。 
# 
#  示例 2： 
# 
#  
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 
# 。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= k <= 100 
#  0 <= prices.length <= 1000 
#  0 <= prices[i] <= 1000 
#  
#  Related Topics 数组 动态规划 👍 749 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, k: int, prices: [int]) -> int:
        '''
        所以定义状态转移数组dp[天数][当前是否持股][卖出的次数]

        '''
        n = len(prices)
        if n < 2:
            return 0

        # distance = [[[0] * n] * n] * n
        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n)]  # (n, 2, k+1)

        # 初始化第一天的交易情况
        for i in range(k + 1):
            dp[0][0][i] = 0
            dp[0][1][i] = -prices[0]

        for i in range(1, n):
            dp[i][0][0] = 0
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][0][0] - prices[i])
            for j in range(1, k + 1):
                dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j] + prices[i])
                dp[i][1][j] = max(dp[i - 1][1][j], dp[i - 1][0][j] - prices[i])

        print(dp)
        return dp[n - 1][0][k]
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    prices = [2, 4, 1]
    k = 2
    out = 6
    S = Solution()
    print(S.maxProfit(k, prices))
