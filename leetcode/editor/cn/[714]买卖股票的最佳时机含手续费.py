# 给定一个整数数组 prices，其中 prices[i]表示第 i 天的股票价格 ；整数 fee 代表了交易股票的手续费用。 
# 
#  你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。 
# 
#  返回获得利润的最大值。 
# 
#  注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出：8
# 解释：能够达到的最大利润:  
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8 
# 
#  示例 2： 
# 
#  
# 输入：prices = [1,3,7,5,10,3], fee = 3
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 5 * 10⁴ 
#  1 <= prices[i] < 5 * 10⁴ 
#  0 <= fee < 5 * 10⁴ 
#  
#  Related Topics 贪心 数组 动态规划 👍 737 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ''' 执行最少次交易，达到最大利润
        这道题「贪心」的地方在于，对于「今天股价-昨天股价」，得到的结果有 3 种可能：① 正数，② 0，③负数。
            把费用归到buy中， buy = prices[i] + fee， 贪心算法的决策是： 只加正数 。
        Time: O(N)
        Space: O(1)
        '''
        n = len(prices)
        buy = prices[0] + fee
        profit = 0

        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit
# leetcode submit region end(Prohibit modification and deletion)
