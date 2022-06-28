# 给定一个整数数组 prices，其中第 prices[i] 表示第 i 天的股票价格 。 
# 
#  设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）: 
# 
#  
#  卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。 
#  
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: prices = [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出] 
# 
#  示例 2: 
# 
#  
# 输入: prices = [1]
# 输出: 0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 5000 
#  0 <= prices[i] <= 1000 
#  
#  Related Topics 数组 动态规划 👍 1239 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        状态：dp[i][j]: 第i天, j表示持股状态
            0.不持股且当天没卖出,没有操作，定义其最大收益dp[i][0];
            1.持股,定义其最大收益dp[i][1]；
            2.不持股且当天卖出了，定义其最大收益dp[i][2]；
        转移方程：
            1. dp[i][0]=max(dp[i-1][0],dp[i-1][2])
        第i天不持股且没卖出的状态dp[i][0], 没有股票且没卖，也就是说i-1也没有股票
        那么第i-1天有两种可能：i-1不持股且当天无卖出dp[i-1][0]，或者，i-1天不持股但当天卖出dp[i-1][2]
            2. dp[i][1] =max(dp[i-1][1]，dp[i-1][0]-prices[i])
        第i天持股的状态dp[i][1], 有股票且没卖，也就是说i-1有股票
        2种可能: i-1持股 dp[i-1][1]，或者，i-1天不持股但当天卖出dp[i-1][0]-prices[i]
            3. dp[i][2] = dp[i-1][1] + prices[i]
        第i天持股的状态dp[i][1], 不持股且当天卖出了，也就是说i-1是有股票
        1种可能: i-1持股 dp[i-1][1] + prices[i]
        初始状态：
            dp[0][0] = 0 第0天不持股，且没卖出，故是0
            dp[0][1] = -1*prices[0] 第0天持股，买股了 收益是-1*prices[0]
            dp[0][2] = 0 第0天不持股，且当天卖出， 那就是买入又卖出， 故收益是0
        返回 return：
            最后一天的最大收益有两种可能，而且一定是“不持有”状态下的两种可能，
            把这两种“不持有”比较一下大小，返回即可
        '''
        n = len(prices)
        dp = [[0 for _ in range(3)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -1 * prices[0]
        dp[0][2] = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]

        return max(dp[-1][0], dp[-1][2])
# leetcode submit region end(Prohibit modification and deletion)
