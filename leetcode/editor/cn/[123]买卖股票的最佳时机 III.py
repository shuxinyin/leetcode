# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。 
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入：prices = [3,3,5,0,0,3,1,4]
# 输出：6
# 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。 
# 
#  示例 2： 
# 
#  
# 输入：prices = [1,2,3,4,5]
# 输出：4
# 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#  
# 
#  示例 3： 
# 
#  
# 输入：prices = [7,6,4,3,1] 
# 输出：0 
# 解释：在这个情况下, 没有交易完成, 所以最大利润为 0。 
# 
#  示例 4： 
# 
#  
# 输入：prices = [1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 10⁵ 
#  0 <= prices[i] <= 10⁵ 
#  
#  Related Topics 数组 动态规划 👍 1146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# reference: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/solution/tong-su-yi-dong-de-dong-tai-gui-hua-jie-fa-by-marc/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' 只执行有限次交易
        状态定义：
            由于我们最多可以完成两笔交易，因此在任意一天结束之后，我们会处于以下五个状态中的一种：
            1.未进行过任何操作；
            2.只进行过一次买操作；
            3.进行了一次买操作和一次卖操作，即完成了一笔交易；
            4.在完成了一笔交易的前提下，进行了第二次买操作；
            5.完成了全部两笔交易。
            状态1的利润显然为 0，不用将其记录。对于剩下的四个状态，我们分别将它们的最大利润记为 buy1，sell1，buy2以及 sell2。
       状态定义：
            buy1 = max(buy1', -prices[i]), buy1'表示第 i−1 天的状态
            sell1 = max(sell1', buy1'+prices[i]), sell1'表示第 i−1 天的状态
            buy2 = max(buy2', sell1'-prices[i]), buy2'表示第 i−1 天的状态
            sell2 = max(sell2', buy2'+prices[i]), sell2'表示第 i−1 天的状态

        另外，无论题目中是否允许「在同一天买入并且卖出」这一操作，最终的答案都不会受到影响，这是因为这一操作带来的收益为零。
        可直接写成下式：
            buy1 = max(buy1, -prices[i]),
            sell1 = max(sell1, buy1+prices[i]),
            buy2 = max(buy2, sell1-prices[i]),
            sell2 = max(sell2, buy2+prices[i]),
        例如在计算 sell1时，我们直接使用 buy1而不是 buy1′进行转移。buy1比 buy1′多考虑的是在第 i 天买入股票的情况，
        而转移到 sell1时，考虑的是在第i天卖出股票的情况，这样在同一天买入并且卖出收益为零，不会对答案产生影响。同理对于buy2 sell2

        T:O(N), S:O(1)
        '''
        n = len(prices)
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for i in range(1, n):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2

    def maxProfit2(self, prices):
        '''
        所以定义状态转移数组dp[天数][当前是否持股][卖出的次数]
        具体一天结束时的6种状态：
            未持股，未卖出过股票：说明从未进行过买卖，利润为0
            dp[i][0][0]=0
            未持股，卖出过1次股票：可能是今天卖出，也可能是之前卖的（昨天也未持股且卖出过）
            dp[i][0][1]=max(dp[i-1][1][0]+prices[i],dp[i-1][0][1])
            未持股，卖出过2次股票:可能是今天卖出，也可能是之前卖的（昨天也未持股且卖出过）
            dp[i][0][2]=max(dp[i-1][1][1]+prices[i],dp[i-1][0][2])
            持股，未卖出过股票：可能是今天买的，也可能是之前买的（昨天也持股）
            dp[i][1][0]=max(dp[i-1][0][0]-prices[i],dp[i-1][1][0])
            持股，卖出过1次股票：可能是今天买的，也可能是之前买的（昨天也持股）
            dp[i][1][1]=max(dp[i-1][0][1]-prices[i],dp[i-1][1][1])
            持股，卖出过2次股票：最多交易2次，这种情况不存在
            dp[i][1][2]=float('-inf')
        '''
        if prices == []:
            return 0
        length = len(prices)
        # 结束时的最高利润=[天数][是否持有股票][卖出次数]
        dp = [[[0, 0, 0], [0, 0, 0]] for i in range(0, length)]
        # 第一天休息
        dp[0][0][0] = 0
        # 第一天买入
        dp[0][1][0] = -prices[0]
        # 第一天不可能已经有卖出
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        # 第一天不可能已经卖出
        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')
        for i in range(1, length):
            # 未持股，未卖出过，说明从未进行过买卖
            dp[i][0][0] = 0
            # 未持股，卖出过1次，可能是今天卖的，可能是之前卖的
            dp[i][0][1] = max(dp[i - 1][1][0] + prices[i], dp[i - 1][0][1])
            # 未持股，卖出过2次，可能是今天卖的，可能是之前卖的
            dp[i][0][2] = max(dp[i - 1][1][1] + prices[i], dp[i - 1][0][2])
            # 持股，未卖出过，可能是今天买的，可能是之前买的
            dp[i][1][0] = max(dp[i - 1][0][0] - prices[i], dp[i - 1][1][0])
            # 持股，卖出过1次，可能是今天买的，可能是之前买的
            dp[i][1][1] = max(dp[i - 1][0][1] - prices[i], dp[i - 1][1][1])
            # 持股，卖出过2次，不可能
            dp[i][1][2] = float('-inf')
        return max(dp[length - 1][0][1], dp[length - 1][0][2], 0)
# leetcode submit region end(Prohibit modification and deletion)
