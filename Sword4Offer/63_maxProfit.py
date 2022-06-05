class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        # Time: O(log(N)), Space: O(1)
        状态定义：列表dp， dp[i]表示以prices[i]为结尾的子数组的最大利润（前i日的最大利润）
        转移方程：前i日的最大利润dp[i] = max(前(i-1)日最大利润， 第i日价格-前i日最低价格)
                    dp[i] = max(dp[i-1], price[i]-min(prices[0:i]))
        初始状态： dp[0]=0, 首日利润为0
        返回值： dp[n-1], 其中n=len(dp)
        '''
        cost, profit = float("+inf"), 0

        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
