# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？ 
# 
#  
# 
#  示例 1: 
# 
#  输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
#  
# 
#  示例 2: 
# 
#  输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。 
# 
#  
# 
#  限制： 
# 
#  0 <= 数组长度 <= 10^5 
# 
#  
# 
#  注意：本题与主站 121 题相同：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-
# stock/ 
#  Related Topics 数组 动态规划 👍 257 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # Time: O(log(N)), Space: O(1)
        状态定义：列表dp， dp[i]表示前i日的交易一次的最大利润
        转移方程：前i日的最大利润dp[i] = max(前(i-1)日最大利润， 第i日价格-前i日最低价格)
                    dp[i] = max(dp[i-1], price[i]-min(prices[0:i]))
        初始状态： dp[0]=0, 首日利润为0
        返回值： dp[n-1], 其中n=len(dp)
        '''
        if not prices:
            return 0
        n = len(prices)
        dp = [0] * n

        for i in range(1, n):
            dp[i] = max(dp[i - 1], prices[i] - min(prices[0:i]))
        return dp[-1]

    def maxProfit2(self, prices: List[int]) -> int:
        ''' 滚动变量
        '''
        cost, profit = float("+inf"), 0

        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
# leetcode submit region end(Prohibit modification and deletion)
